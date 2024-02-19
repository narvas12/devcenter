from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CompletedTasksAPIView

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path('', include(router.urls)),
    path('completed_tasks', CompletedTasksAPIView.as_view(), name="completed_tasks"),
]
