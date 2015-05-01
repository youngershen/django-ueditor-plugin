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
from .models import UeditorFile
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

    def __init__(self, *args, **kwargs):
        self.config = get_config()
        super(ControllerView, self).__init__(*args, **kwargs)

    def get(self, request, *args, **kwarg):
        action_data = self.get_action(request)
        if action_data:
            return self.render_to_response(action_data)
        else:
            raise Http404

    def get_context_data(self):
        return self.config

    def post(self, request, *args, **kwargs):
        action_data = self.get_action(request, *args, **kwargs)
        if action_data:
            return self.render_to_response(action_data)
        else:
            raise Http404

    def config_action(self, request):
        return self.config

    def get_action(self, request):
        action = request.GET.get('action', '')
        action_method = getattr(self, action + '_action')
        if action_method:
            return action_method(request)
        return None

    def listfile_action(self, request):
        allow_file_types = self.config.get('fileManagerAllowFiles')
        default_size = self.config.get('fileManagerListSize')
        size = request.GET.get('size', '')
        start = request.GET.get('start', 0)
        try:
            size = int(size)
        except (ValueError, TypeError):
            size = default_size

        end = int(start) + size
        files = UeditorFile.objects.filter(type__in=allow_file_types).values_list('url', flat=True)
        import random
        files_list = map(lambda x: {'url': x, 'mtime': random.random()}, files[start: end])

        if files.exists():
            return {'state': 'SUCCESS',
                    'list': files_list,
                    'start': start,
                    'total': files.count()
                    }
        else:
            return {'state': 'no match files',
                    'list': [],
                    'start': start,
                    'total': 0
                    }

    def listimage_action(self, request):
        allow_file_types = self.config.get('imageManagerAllowFiles')
        default_size = self.config.get('imageManagerListSize')
        size = request.GET.get('size', '')
        start = request.GET.get('start', 0)
        try:
            size = int(size)
        except (ValueError, TypeError):
            size = default_size

        end = int(start) + size
        files = UeditorFile.objects.filter(type__in=allow_file_types).values_list('url', flat=True)
        import random
        files_list = map(lambda x: {'url': x, 'mtime': random.random()}, files[start: end])

        if files.exists():
            return {'state': 'SUCCESS',
                    'list': files_list,
                    'start': start,
                    'total': files.count()
                    }
        else:
            return {'state': 'no match files',
                    'list': [],
                    'start': start,
                    'total': 0
                    }

    def uploadimage_action(self, request):
        config = self.config

        uploadimage_config = {'pathFormat': config.get('imagePathFormat', ''),
                              'maxSize': config.get('imageMaxSize', ''),
                              'allowFiles': config.get('imageAllowFiles', ''),
                              'fieldName': config.get('imageFieldName', '')
                              }

        return upload_file(request, uploadimage_config)

    def uploadscrawl_action(self, request):
        config = self.config

        uploadscrawl_config = {'pathFormat': config.get('scrawlPathFormat', ''),
                               'maxSize': config.get('scrawlMaxSize', ''),
                               'allowFiles': config.get('scrawlAllowFiles', ''),
                               'oriName': config.get('scrawOriName', 'scrawl.png'),
                               'fieldName': config.get('scrawlFieldName', ''),
                               'base64': 'base64'
                               }

        return upload_file(request, uploadscrawl_config, base64='base64')

    def uploadvideo_action(self, request):
        config = self.config

        uploadvideo_config = {'pathFormat': config.get('videoPathFormat', ''),
                              'maxSize': config.get('videoMaxSize', ''),
                              'allowFiles': config.get('videoAllowFiles', ''),
                              'fieldName': config.get('videoFieldName', ''),
                              }

        return upload_file(request, uploadvideo_config)

    def uploadfile_action(self, request):
        config = self.config

        uploadfile_config = {'pathFormat': config.get('filePathFormat', ''),
                             'maxSize': config.get('fileMaxSize', ''),
                             'allowFiles': config.get('fileAllowFiles', ''),
                             'fieldName': config.get('fileFieldName', '')
                             }

        return upload_file(request, uploadfile_config)

controller_view = csrf_exempt(ControllerView.as_view())