# -*- coding: utf-8 -*-

# This will force all string to be unicode strings, even if we don't
# set the 'u'
from __future__ import unicode_literals

# Django modules imports
from django import forms
from django.utils.translation import ugettext as _

import timedelta

# Tundle modules imports
from tickets.models import (
    Ticket
)