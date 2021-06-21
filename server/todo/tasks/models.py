"""Todo list models."""

# Django
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

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