from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Load purple_martin app urls.py
                       url(r'^', include('purple_martin.urls')),
                       # urls for login
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       #admin urls
                       url(r'^admin/', include(admin.site.urls)),
)
