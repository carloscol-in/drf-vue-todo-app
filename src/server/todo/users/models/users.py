"""Users models."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Utilities
from todo.utils.models import TodoModel


class User(TodoModel):
    """User model."""

    email = models.EmailField(
        _('user email'),
        unique=True,
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        _('User first name'),
        max_length=50,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        _('user last name'),
        max_length=50,
        blank=True,
        null=True
    )