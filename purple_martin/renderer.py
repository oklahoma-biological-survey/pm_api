__author__ = 'mstacy'
from rest_framework.renderers import BrowsableAPIRenderer

class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
    #def get_default_renderer(self, view):
    #    return JSONRenderer()
    format = 'custom_api'
    template = 'rest_framework/custom.html'
    def get_context(self, data, accepted_media_type, renderer_context):
        context= super(CustomBrowsableAPIRenderer,self).get_context(data, accepted_media_type, renderer_context)
        if type([])==type(data):
            context['content']=data
        else:
            context['content']=[data,]
        return context