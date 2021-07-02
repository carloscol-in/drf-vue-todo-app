"""Utilities models."""

# Django
from django.utils.translation import gettext_lazy as _
from django.db import models


class TodoModel(models.Model):
    """Todo model."""

    created = models.DateTimeField(
        _('created at date'),
        auto_now_add=True,
        help_text='Date time at which the object was created'
    )
    modified = models.DateTimeField(
        _('modified at date'),
        auto_now=True,
        help_text='Date at which the object was modified for the last time'
    )

    class Meta:
        """Meta options"""

        abstract=True

        get_latest_by='created'
        ordering=('-created', '-modified')