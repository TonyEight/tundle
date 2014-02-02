# coding=utf-8

# Built-in modules imports
import os

# Django modules imports
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

# Tundle modules imports
from attachments.models import Attachment

# We listen to the post_delete signal
# If emitted, we fire an auto_delete_file function
@receiver(models.signals.post_delete, sender=Attachment)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem when the 
    Attachment instance is deleted.

    """
    # First, we make sure the instance of Attachment has
    # a file defined (even if this attribute is required)
    if instance.file:
        # We ensure, at the filesystem level that the path we found
        # for this instance.file is a file
        if os.path.isfile(instance.file.path):
            # Then we remove it
            os.remove(instance.file.path)


# We listen to the pre_save signal
# If emitted, we fire an auto_delete_file function
@receiver(models.signals.pre_save, sender=Attachment)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem when the 
    FileField in the Attachment instance is modified.

    """
    # If the signal has been sent on create,we do nothing. 
    # We know it is a create since there is no 'pk'
    if instance.pk:
        # We make sure the Attachment object stored in the database
        # has a file defined (even if this attribute is required)
        # If it not defined, no deletion is required
        try:
            attachment = Attachment.objects.get(pk=instance.pk)
            if attachment.file:
                # We retrieve the file defined before the change
                old_file = attachment.file
                # Then we compare it to the new defined file
                if not old_file == instance.file:
                    # If they are different, it means the old one has been 
                    # replaced by the new instance.file, so we can remove it
                    # We ensure, at the filesystem level that the path we 
                    # found for this instance.file is a file
                    if os.path.isfile(old_file.path):
                        # Then we remove it
                        os.remove(old_file.path)
        # We do nothing if we can't retrieve the Attachment 
        # object from the database
        except Attachment.DoesNotExist:
            return False