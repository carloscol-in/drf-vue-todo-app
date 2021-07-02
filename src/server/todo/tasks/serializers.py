"""Todo serializers."""

# DRF
from rest_framework import serializers

# Models
from todo.tasks.models import Task

# Serializers
from todo.users.serializers import UserModelSerializer

class TasksModelSerializer(serializers.ModelSerializer):
    """Task model serializer."""

    creator = UserModelSerializer(read_only=True)

    class Meta:
        """Meta options."""

        model = Task
        fields = '__all__'
        read_only_fields = ('user',)