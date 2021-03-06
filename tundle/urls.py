# coding=utf-8

# This will force all string to be unicode strings, even if we don't
# set the 'u'
from __future__ import unicode_literals

# Django modules imports
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Frontend URLs
    url(r'^', include('frontend.urls')),

    # Admin URLs
    url(r'^admin/', include(admin.site.urls)),
)
