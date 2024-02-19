from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class CompletedTaskListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        completed_tasks = Task.objects.filter(completed=True, owner=request.user)
        serializer = TaskSerializer(completed_tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        task = Task.objects.get(pk=pk, owner=request.user)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = Task.objects.get(pk=pk, owner=request.user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# questrion7:
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    


