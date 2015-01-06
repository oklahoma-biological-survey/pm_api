__author__ = 'mstacy'
from django.conf.urls import patterns, include, url
from rest_framework import routers

from purple_martin.views import RoostViewSet, LuSourceViewSet


router = routers.DefaultRouter()
router.register('roosts', RoostViewSet)
router.register('lusource', LuSourceViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)