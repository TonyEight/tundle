# coding=utf-8

# This will force all string to be unicode strings, even if we don't
# set the 'u'
from __future__ import unicode_literals

# Django modules imports
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.db import models

# Third-party modules imports
from pagedown.widgets import AdminPagedownWidget

# Tundle modules imports
from attachments.models import Attachment

class AttachmentAdmin(admin.ModelAdmin):
    """Activates attachments management from the Admin Interface."""
    # Explicitely set all fields available by declaring the 
    # read-only fields
    readonly_fields = ('ticket',)

    # Set fields order and fieldsets
    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': (
                'file',
                'description',
                'ticket',
            )
        }),
    )

    # Set the list of fields to display in the change list page
    list_display = (
        'ticket',
        'filename',
    )

    # Set the list of fields which will act as links to the 
    # ticket edit page
    list_display_links = (
        'filename',
    )

    # Set the fields over which the search form will perform the search
    search_fields = (
        'filename',
        'file',
        'description',
    )

    # Set PageDown editor on all TextField
    # In fact, this only concerns the description field
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

# Registers all models
admin.site.register(Attachment, AttachmentAdmin)