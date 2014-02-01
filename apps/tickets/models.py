# -*- coding: utf-8 -*-

# This will force all string to be unicode strings, even if we don't
# set the 'u'
from __future__ import unicode_literals

# Django modules imports
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

# Third-party modules imports
import timedelta

class Severity(models.Model):
    """This model stores severity levels.

    It is used to specify the seriousness of the issue the ticket is
    about.

    """
    # We use the nested Meta class to add some verbosity to our model
    class Meta:
        verbose_name = _('Severity')
        verbose_name_plural = _('Severities')

    # Attributes - our model fields
    label = models.CharField(max_length=255, unique=True, 
                             verbose_name=_('label'))
    weight = models.PositiveIntegerField(unique=True, 
                                         verbose_name=_('weight'))

    # Methods
    def __unicode__(self):
        """This method simply returns a human readable value for the
        Python object representing our model.

        Here it returns the label of the severity level.

        """
        return _('%(label)s' % {'label': self.label})

class Priority(models.Model):
    """This model stores priority levels.

    It is used to specify the prioritisation of the ticket in the global
    workload and the planning.

    """
    # We use the nested Meta class to add some verbosity to our model
    class Meta:
        verbose_name = _('Priority')
        verbose_name_plural = _('Priorities')

    # Attributes - our model fields
    label = models.CharField(max_length=255, unique=True, 
                             verbose_name=_('label'))
    weight = models.PositiveIntegerField(unique=True, 
                                         verbose_name=_('weight'))

    # Methods
    def __unicode__(self):
        """This method simply returns a human readable value for the
        Python object representing our model.

        Here it returns the label of the priority level.

        """
        return _('%(label)s' % {'label': self.label})

class Status(models.Model):
    """This model stores ticket status.

    It is used to specify the actual state of the ticket.

    """
    # We use the nested Meta class to add some verbosity to our model
    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Status')

    # Attributes - our model fields
    label = models.CharField(max_length=255, unique=True, 
                             verbose_name=_('label'))

    # Methods
    def __unicode__(self):
        """This method simply returns a human readable value for the
        Python object representing our model.

        Here it returns the label of the status.

        """
        return _('%(label)s' % {'label': self.label})

class Domain(models.Model):
    """This model stores ticket main domains.

    It can be the domain or the project for which the issue has been raised.

    """
    # We use the nested Meta class to add some verbosity to our model
    class Meta:
        verbose_name = _('Domain')
        verbose_name_plural = _('Domains')

    # Attributes - our model fields
    label = models.CharField(max_length=255, unique=True, 
                             verbose_name=_('label'))

    # Methods
    def __unicode__(self):
        """This method simply returns a human readable value for the
        Python object representing our model.

        Here it returns the label of the domain.

        """
        return _('%(label)s' % {'label': self.label})

class SubDomain(models.Model):
    """This model stores ticket subdomains.

    It can be the subdomain or the module for which the issue has been 
    raised.

    """
    # We use the nested Meta class to add some verbosity to our model
    class Meta:
        verbose_name = _('SubDomain')
        verbose_name_plural = _('SubDomains')

    # Attributes - our model fields
    domain = models.ForeignKey(Domain, verbose_name=_('domain'), 
                               related_name='subdomains')
    label = models.CharField(max_length=255, unique=True, 
                             verbose_name=_('label'))

    # Methods
    def __unicode__(self):
        """This method simply returns a human readable value for the
        Python object representing our model.

        Here it returns the label of the subdomain.

        """
        return _('%(label)s' % {'label': self.label})

class Ticket(models.Model):
    """This model stores tickets."""
    # We use the nested Meta class to add some verbosity to our model
    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')

    # Attributes - our model fields
    # Most of the fields are not required. We will use this to implement
    # smart ticket forms based on a workflows mechanism.
    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    owner = models.ForeignKey(User, verbose_name=_('owner'), null=True, 
                              blank=True)
    author = models.ForeignKey(User, verbose_name=_('author'), 
                               related_name='created_tickets')
    domain = models.ForeignKey(Domain, verbose_name=_('domain'), null=True, 
                               blank=True)
    subdomain = models.ForeignKey(SubDomain, verbose_name=_('subdomain'), 
                                  null=True, blank=True)
    status = models.ForeignKey(Status, verbose_name=_('status'))
    severity = models.ForeignKey(Severity, verbose_name=_('severity'), 
                                 null=True, blank=True)
    priority = models.ForeignKey(Priority, verbose_name=_('priority'), 
                                 null=True, blank=True)
    deadline = models.DateTimeField(verbose_name=_('deadline'), null=True, 
                                    blank=True)
    copy_to = models.ManyToManyField(User, verbose_name=_('copy_to'), 
                                     related_name='followed_tickets', 
                                     null=True, blank=True)
    planned_start = models.DateTimeField(verbose_name=_('planned_start'), 
                                         null=True, blank=True)
    planned_end = models.DateTimeField(verbose_name=_('planned_end'), 
                                       null=True, blank=True)
    planned_workload = timedelta.fields.TimedeltaField(
                                        verbose_name=_('planned_workload'),
                                        null=True, blank=True)
    related_tickets = models.ManyToManyField('self', 
                                        verbose_name=_('related_tickets'),
                                        null=True, blank=True)
    parent_ticket = models.ForeignKey('self', 
                                      verbose_name=_('parent_ticket'),
                                      null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, 
                                      verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, 
                                      verbose_name=_('updated at'))

    # Methods
    def __unicode__(self):
        """This method simply returns a human readable value for the 
        Python object representing our model.

        Here it returns the ticket number which is no other than 
        its own primary_key.

        """
        return _('ticket #%(ticket_id)d' % {'ticket_id': self.pk})

    def clean(self):
        """Validates the ticket fields.

        We override the default clean() method to add custom validation 
        for our model. It will ensure its integrity regarding our project 
        logic.

        """
        # If a subdomain has been set, so the domain must be set too
        if self.subdomain is not None and self.domain is None:
            raise ValidationError(_('Cannot save a ticket with a subdomain '
                                    'but no domain specified.'))

        # Here, we check severals conditions over the planned time
        # if both dates are specified
        if self.planned_start is not None and self.planned_end is not None:
            # First we validate the dates logic
            # The planned end must be greater than or equal to the planned 
            # start
            if self.planned_start > self.planned_end:
                raise ValidationError(_('Cannot set a planned start later '
                                        ' than the planned end.'))
            # Then we validate the planned workload value if it's specified
            # in addition to the planned dates
            if self.planned_workload is not None:
                # The planned workload cannot represent more time than the
                # delta between the planned start and the planned end
                delta = self.planned_end - self.planned_start
                if self.planned_workload > delta:
                    raise ValidationError(_('Cannot save a ticket with a '
                                            'subdomain but no domain '
                                            'specified.'))

        # A ticket can be either related to another or parent of another
        # but not both
        if self.parent_ticket is not None and self.related_tickets is not None:
            if self.parent_ticket in self.related_tickets:
                raise ValidationError(_('A ticket cannot be parent '
                                        'and related to another ticket '
                                        'at the same time.'))    
