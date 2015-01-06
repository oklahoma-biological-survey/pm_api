#from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.renderers import BrowsableAPIRenderer, JSONPRenderer,JSONRenderer,XMLRenderer,YAMLRenderer #, filters
from renderer import CustomBrowsableAPIRenderer
from filters import RoostsFilter
from purple_martin.models import Roosts, LuSource
from serializer import RoostSerializer, LuSourceSerializer


class RoostViewSet(viewsets.ModelViewSet):
    """
    This is the roost list with source table hyperlinked.


    """
    model = Roosts
    queryset = Roosts.objects.all()
    serializer_class = RoostSerializer
    renderer_classes = (BrowsableAPIRenderer,CustomBrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = RoostsFilter
    search_fields = ('name', 'loc_source_comment',)
    ordering_fields = ('name', 'loc_source_comment', 'latitude', 'longitude', 'source_no','source__cource')

class LuSourceViewSet(viewsets.ModelViewSet):
    model = LuSource
    queryset = LuSource.objects.all() #.using('purple').all()
    serializer_class = LuSourceSerializer