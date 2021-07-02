"""Todo urls."""

# Django
from django.urls import path, include

# DRF
from rest_framework.routers import DefaultRouter

# Views
from todo.tasks import views as tasks_views


router = DefaultRouter()
router.register(r'tasks', tasks_views.TasksViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]