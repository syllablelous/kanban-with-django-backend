from rest_framework import serializers
from apps.tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'task_name',
            'description',
            'status',
            'due_date',
        ]