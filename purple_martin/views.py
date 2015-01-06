from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework import viewsets
from rest_framework.renderers import BrowsableAPIRenderer, JSONPRenderer,JSONRenderer,XMLRenderer,YAMLRenderer #, filters
from renderer import CustomBrowsableAPIRenderer

from purple_martin.models import Roosts, LuSource
from serializer import RoostSerializer, LuSourceSerializer #,Roost_embedSerializer#, DoeFilter


class RoostViewSet(viewsets.ModelViewSet):
    """
    This is the roost list with source table hyperlinked.
    """
    model = Roosts
    queryset = Roosts.objects.all() #.using('purple').all()
    serializer_class = RoostSerializer
    renderer_classes = (BrowsableAPIRenderer,CustomBrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    #filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    #filter_class = DoeFilter
    #search_fields = ('county', 'site_number', 'referent', 'agency',)
    #ordering_fields = ('county', 'site_number', 'dertermination', 'referent', 'agency')

class LuSourceViewSet(viewsets.ModelViewSet):
    model = LuSource
    queryset = LuSource.objects.all() #.using('purple').all()
    serializer_class = LuSourceSerializer