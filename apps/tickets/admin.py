# -*- coding: utf-8 -*-

# This will force all string to be unicode strings, even if we don't
# set the 'u'
from __future__ import unicode_literals

# Django modules imports
from django.contrib import admin
from django.utils.translation import ugettext as _

# Tundle modules imports
from tickets.models import (
    Severity,
    Priority,
    Status,
    Domain,
    SubDomain,
    Ticket
)

class SeverityAdmin(admin.ModelAdmin):
    """Activates severity levels management from the Admin Interface."""
    # Set fields order and fieldsets
    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': (
                'label', 
                'weight',
            )
        }),
    )

    # Set the list of fields to display in the change list page
    list_display = (
        'label', 
        'weight',
    )

    # Set the list of fields which will act as links to the 
    # ticket edit page
    list_display_links = (
        'label',
    )

class PriorityAdmin(admin.ModelAdmin):
    """Activates priority levels management from the Admin Interface."""
    # Set fields order and fieldsets
    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': (
                'label', 
                'weight',
            )
        }),
    )

    # Set the list of fields to display in the change list page
    list_display = (
        'label', 
        'weight',
    )

    # Set the list of fields which will act as links to the 
    # ticket edit page
    list_display_links = (
        'label',
    )

class StatusAdmin(admin.ModelAdmin):
    """Activates status management from the Admin Interface."""
    # Set fields order and fieldsets
    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': (
                'label', 
            )
        }),
    )

    # Set the list of fields to display in the change list page
    list_display = (
        'label',
    )

    # Set the list of fields which will act as links to the 
    # ticket edit page
    list_display_links = (
        'label',
    )

class DomainAdmin(admin.ModelAdmin):
    """Activates domains management from the Admin Interface."""
    # Set fields order and fieldsets
    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': (
                'label', 
            )
        }),
    )

    # Set the list of fields to display in the change list page
    list_display = (
        'label',
    )

    # Set the list of fields which will act as links to the 
    # ticket edit page
    list_display_links = (
        'label',
    )

class SubDomainAdmin(admin.ModelAdmin):
    """Activates subdomains management from the Admin Interface."""
    # Set fields order and fieldsets
    fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': (
                'domain',
                'label', 
            )
        }),
    )

    # Set the list of fields to display in the change list page
    list_display = (
        'domain',
        'label',
    )

    # Set the list of fields which will act as links to the 
    # ticket edit page
    list_display_links = (
        'label',
    )

class TicketAdmin(admin.ModelAdmin):
    """Activates tickets management from the Admin Interface."""
    # Explicitely set all fields available by declaring the 
    # read-only fields
    readonly_fields = ('created_at', 'updated_at')
    
    # Set fields order and fieldsets
    fieldsets = (
        ('General', {
            'classes': ('wide', 'extrapretty'),
            'fields': (
                'title', 
                'description', 
                'author',
                ('owner', 'status',),
                ('created_at', 'updated_at',),
            )
        }),
        ('Is about', {
            'classes': ('wide', 'extrapretty'),
            'fields': (
                ('domain', 'subdomain',),
                'parent_ticket',
                'is_linked_to',
            )
        }),
        ('Request', {
            'classes': ('wide', 'extrapretty'),
            'fields': (
                ('severity', 'deadline',),
                'copy_to',
            )
        }),
        ('Response', {
            'classes': ('wide', 'extrapretty'),
            'fields': (
                'planned_workload', 
                ('planned_start','planned_end',),
                'priority',
            )
        }),
    )
    
    # Use horizontal filter for ManyToManyField
    filter_horizontal = ('copy_to',)

    # Set the list of fields to display in the change list page
    list_display = (
        'ticket_number',
        'title',
        'author',
        'owner',
        'status',
        'created_at',
        'updated_at',
        'domain',
        'subdomain',
        'priority',
    )

    # Set the list of fields which will act as links to the 
    # ticket edit page
    list_display_links = (
        'ticket_number',
        'title',
    )

    # Set a list of filters for the change list page
    list_filter = (
        'author',
        'owner',
        'status',
        'domain',
        'subdomain',
        'priority',
    )

    # Set the 'save' buttons to appear both on the top and the 
    # bottom of the form
    save_on_top = True

    # Set the fields over which the search form will perform the search
    search_fields = (
        'ticket_number',
        'title',
        'description',
    )

# Registers all models
admin.site.register(Severity, SeverityAdmin)
admin.site.register(Priority, PriorityAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(SubDomain, SubDomainAdmin)
admin.site.register(Ticket, TicketAdmin)