from rest_framework import viewsets

from .serializers import TaskSerializer

from .models import Task


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
