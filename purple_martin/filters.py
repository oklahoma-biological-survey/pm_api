__author__ = 'mstacy'
import django_filters

from models import Roosts

class RoostsFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_type='icontains')
    min_lat = django_filters.NumberFilter(name='latitude',lookup_type='gte')
    max_lat = django_filters.NumberFilter(name='latitude',lookup_type='lte')
    min_long = django_filters.NumberFilter(name='longitude',lookup_type='gte')
    max_long = django_filters.NumberFilter(name='longitude',lookup_type='lte')
    cource = django_filters.CharFilter(name='source__cource', lookup_type='icontains')
    loc_source_comment = django_filters.CharFilter(lookup_type='icontains')

    class Meta:
        model = Roosts
        fields = ['name', 'loc_source_comment',]