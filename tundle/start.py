# coding=utf-8

# This will force all string to be unicode strings, even if we don't
# set the 'u'
from __future__ import unicode_literals

# Django modules imports
from django.conf import settings
from django.utils.importlib import import_module
from django.utils.module_loading import module_has_submodule
from django.utils.translation import ugettext_lazy as _

def autoload(submodules):
    """Loads the given modules."""
    for app in settings.INSTALLED_APPS:
        mod = import_module(app)
        for submodule in submodules:
            try:
                import_module("{0}.{1}".format(app, submodule))
            except:
                if module_has_submodule(mod, submodule):
                    raise

def run():
    """Is executed on startup from wsgi.py."""
    autoload(["signals"])