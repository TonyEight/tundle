# coding=utf-8

# This will force all string to be unicode strings, even if we don't
# set the 'u'
from __future__ import unicode_literals

# Django modules imports
from django.conf.urls import patterns, include, url

# Tundle modules imports
from frontend.views import DashboardView

urlpatterns = patterns('',
    # Dashboard
    url(r'^$', DashboardView.as_view(), name='dashboard'),
)
