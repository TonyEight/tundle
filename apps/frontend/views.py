# coding=utf-8

# This will force all string to be unicode strings, even if we don't
# set the 'u'
from __future__ import unicode_literals

# Django modules imports
from django.views.generic import TemplateView

class DashboardView(TemplateView):
	template_name = "frontend/base.html"