# coding=utf-8

# This will force all string to be unicode strings, even if we don't
# set the 'u'
from __future__ import unicode_literals

# Built-in modules imports
import os

# Django modules imports
from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings
from django.core.exceptions import ValidationError

# Tundle modules imports
from demands.models import Ticket

def store_attachment(filename, instance):
    return '/'.join(['attachments', 
                     instance.ticket.ticket_number,
                     filename])

class Attachment(models.Model):
    """This model stores attachments.

    It is used to add documents or images to a ticket as it offers
    more details.

    """
    # We use the nested Meta class to add some verbosity to our model
    class Meta:
        verbose_name = _('Attachment')
        verbose_name_plural = _('Attachments')

    # Attributes - our model fields
    ticket = models.ForeignKey(Ticket, verbose_name=_('ticket'))
    file = models.FileField(upload_to=store_attachment, 
                            verbose_name=_('file'))
    description = models.TextField(verbose_name=_('description'),
                                   blank=True)

    # Methods
    def __unicode__(self):
        """This method simply returns a human readable value for the
        Python object representing our model.

        Here it returns the filename and the related ticket number.

        """
        return _('%(filename)s (%(ticket_number)s)' % 
                 {'ticket_number': self.ticket.ticket_number,
                 'filename': self.filename})

    def _get_filename(self):
        """Returns the attachment."""
        return os.path.basename(self.file.name)

    # Creates the property filename which exposes the result of
    # the _get_filename method
    filename = property(_get_filename)

    def clean(self):
        """Validates the attachment fields.

        We override the default clean() method to add custom validation 
        for our model. It will ensure its integrity regarding our project 
        logic.

        """
        # First, we make sure self.file has a content_type attribute
        if hasattr(self.file, 'content_type'):
            content_type = self.file.content_type
            # We check the content type against the content types list
            # from the settings
            if content_type in settings.ATTACHMENT_CONTENT_TYPES:
                # If the file type is valid, we make sure 
                # self.file has a _size attribute
                if hasattr(self.file, '_size'):
                    # Then, we check the size against the maximum 
                    # allowed size value from the settings
                    if self.file._size > settings.ATTACHMENT_MAX_SIZE:
                        raise ValidationError(_('The uploaded file size '
                                                '(%(file_size)s) is over '
                                                'the maximum size allowed '
                                                '(%(max_size)s).' % 
                                                {'max_size': filesizeformat(
                                                    settings\
                                                    .ATTACHMENT_MAX_SIZE), 
                                                 'file_size': filesizeformat(
                                                    self.file._size)}))
            else:
                raise ValidationError(_('This file type is not supported.'))
