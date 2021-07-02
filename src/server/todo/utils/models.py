"""Utilities models."""

# Django
from django.utils.translation import gettext_lazy as _
from django.db import models


class TodoModel(models.Model):
    """Todo abstract model.
    
    All models in this project will inherit at least from this
    model."""

    created = models.DateTimeField(
        'Created at',
        auto_now_add=True,
        help_text="Date and time at which the task was created"
    )
    modified = models.DateTimeField(
        'Modified at',
        auto_now=True,
        help_text="Date and time at which the task was last modified"
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ('-created', '-modified')