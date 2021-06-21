"""Todo views."""

# DRF
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

# Models
from todo.tasks.models import Task

# Serializers
from todo.tasks.serializers import TasksModelSerializer


class TasksViewSet(
        mixins.ListModelMixin,
        viewsets.GenericViewSet,
    ):
    """Tasks viewset."""

    serializer_class = TasksModelSerializer


    def get_queryset(self):
        """Get the queryset to return some objects."""
        queryset = Task.objects.all()

        if self.action == 'list':
            return queryset.filter(is_complete=False)

        return queryset

    def get_permissions(self):
        """Get permissions for this view."""

        permissions = [IsAuthenticated]

        return [p() for p in permissions]