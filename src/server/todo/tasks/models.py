"""Todo list models."""

# Django
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Utilities
from todo.utils.models import TodoModel


class Task(TodoModel):
    """Task model."""

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        'Task to complete',
        max_length=255,
    )

    description = models.TextField(
        'Description of the task',
        max_length=500,
    )

    is_complete = models.BooleanField(
        'Is task complete?',
        default=False,
        help_text="This property is used to distinguish from completed tasks"
    )

    completed_at = models.DateTimeField(
        'Completed at',
        null=True,
        blank=True,
        help_text="Date and time at which the taxt was completed"
    )