# tasks/views.py
from rest_framework import viewsets, generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTaskOwner

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskOwner]

class CompletedTasksAPIView(generics.ListAPIView):
    queryset = Task.objects.filter(completed=True)
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]