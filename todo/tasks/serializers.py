"""Todo serializers."""

# DRF
from rest_framework import serializers

from todo.tasks.models import Task

class TasksModelSerializer(serializers.ModelSerializer):
    """Task model serializer."""

    class Meta:
        """Meta options."""

        model = Task
        fields = '__all__'
        read_only_fields = ('user',)