# -*- coding:utf-8 -*-
# PROJECT_NAME : django-ueditor-plugin
# FILE_NAME    :
# AUTHOR       : younger shen
import json
from django.views.generic import View
from django.http import HttpResponse, Http404
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from .utils import get_config
from .utils import upload_file
# Create your views here.


class JsonResponse(HttpResponse):
    def __init__(self, context=None, encoder=DjangoJSONEncoder, safe=True, **kwargs):
        if safe and not isinstance(context, dict):
            raise TypeError('In order to allow non-dict objects to be '
                            'serialized set the safe parameter to False')

        data = json.dumps(context, cls=encoder)
        kwargs.setdefault('content_type', 'application/json')
        super(JsonResponse, self).__init__(content=data, **kwargs)


class JsonResponseMixin(object):
    content_type = 'application/json'
    response_class = JsonResponse

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(context=context, **response_kwargs)


class JsonView(View, JsonResponseMixin):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return self.render_to_response(context)


class ControllerView(JsonView):

    def get(self, request, *args, **kwarg):
        callback = request.GET.get('callback', None)
        action = request.GET.get('action', None)
        config = get_config()

        if 'config' == action:
            return HttpResponse(json.dumps(config))

        if callback:
            return HttpResponse(callback + '(' + json.dumps(config) + ')')
        else:
            return HttpResponse(json.dumps(dict(state=u"callback参数不合法")))

    def get_context_data(self):
        return self.config_action()

    def post(self, request, *args, **kwargs):
        action_data = self.get_action(request, *args, **kwargs)
        if action_data:
            return self.render_to_response(action_data)
        else:
            raise Http404

    def get_action(self, request):
        action = request.GET.get('action', '')
        action_method = getattr(self, action + '_action')
        if action_method:
            return action_method(request)
        return None

    def config_action(self):
        return get_config()

    def uploadimage_action(self, request):
        config = self.config_action()

        uploadimage_config = {'pathFormat': config.get('imagePathFormat', ''),
                              'maxSize': config.get('imageMaxSize', ''),
                              'allowFiles': config.get('imageAllowFiles', ''),
                              'fieldName': config.get('imageFieldName', '')
                              }

        return upload_file(request, uploadimage_config)

    def uploadscrawl_action(self, request):
        config = self.config_action()

        uploadscrawl_config = {'pathFormat': config.get('scrawlPathFormat', ''),
                               'maxSize': config.get('scrawlMaxSize', ''),
                               'allowFiles': config.get('scrawlAllowFiles', ''),
                               'oriName': config.get('scrawl.png', ''),
                               'fieldName': config.get('scrawlFieldName', ''),
                               'base64': 'base64'
                               }

        return upload_file(request, uploadscrawl_config)

    def uploadvideo_action(self, request):
        config = self.config_action()

        uploadvideo_config = {'pathFormat': config.get('videoPathFormat', ''),
                              'maxSize': config.get('videoMaxSize', ''),
                              'allowFiles': config.get('videoAllowFiles', ''),
                              'fieldName': config.get('videoFieldName', ''),
                              }

        return upload_file(request, uploadvideo_config)

    def uploadfile_action(self, request):
        config = self.config_action()

        uploadfile_config = {'pathFormat': config.get('filePathFormat', ''),
                             'maxSize': config.get('fileMaxSize', ''),
                             'allowFiles': config.get('fileAllowFiles', ''),
                             'fieldName': config.get('fileFieldName', '')
                             }

        return upload_file(request, uploadfile_config)

controller_view = csrf_exempt(ControllerView.as_view())