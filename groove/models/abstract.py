from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimestampedModel(models.Model):
    """
    Abstract class that automatically adds timestamps upon creation and
    modification.
    """

    creation_time = models.DateTimeField(_('creation time'), auto_now_add=True)
    modification_time = models.DateTimeField(_('modification time'), auto_now=True)

    class Meta:
        abstract = True
