from rest_framework import viewsets

from .serializers import TaskReadSerializer, TaskSerializer

from .models import Task


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TaskReadSerializer
        return TaskSerializer
