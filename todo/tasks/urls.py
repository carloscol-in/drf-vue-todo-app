"""Todo urls."""

# django
from django.urls import path

# Views
from todo.tasks.views import TasksViewSet


urlpatterns = [
    path('todo/', TasksViewSet.as_view(), name='todo'),
]