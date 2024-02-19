from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CompletedTaskView

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path('', include(router.urls)),
    path('completed_tasks', CompletedTaskView.as_view, name="completed_tasks"),
]
