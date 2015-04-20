import json
from django.views.generic import View
from django.http import HttpResponse, Http404
from django.core.serializers.json import DjangoJSONEncoder
from .utils import get_config
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

    def get(self, request, *args, **kwargs):
        action_data = self.get_action(request, *args, **kwargs)
        if action_data:
            return self.render_to_response(action_data)
        else:
            raise Http404

    def get_action(self, request, *args, **kwargs):
        action = request.GET.get('action', None)
        if action:
            if 'config' == action:
                return self.config_action(request)

            elif 'uploadimage' == action:
                pass
            elif 'uploadscrawl' == action:
                pass

            elif 'uploadvideo' == action:
                pass

            elif 'uploadfile' == action:
                pass

            elif 'listimage' == action:
                pass

            elif 'listfile' == action:
                pass

            elif 'catchimage' == action:
                pass
            else:
                return None

        else:
            return None

    def config_action(self, request):
        return get_config()

    def uploadimage_action(self, request):
        print request
        return self

controller_view = ControllerView.as_view()