from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    executor = serializers.StringRelatedField()
    projects = serializers.StringRelatedField(
        many=True,
        read_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'create_dt',
            'deadline_dt',
            'executor',
            'priority',
            'title',
            'comment',
            'projects',
        ]
