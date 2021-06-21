"""Tasks admin."""

# Django
from django.contrib import admin

# Models
from todo.tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    """Task model admin manager."""

    list_display = (
        'creator',
        'name',
        'description',
        'is_complete',
    )
    list_display_links = (
        'description'
    )
    list_editable = (
        'name',
        'is_complete',
    )