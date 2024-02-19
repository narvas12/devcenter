from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CompletedTaskListView

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path('', include(router.urls)),
    path('completed_tasks', CompletedTaskListView.as_view, name="completed_tasks"),
]
