from ...models import Task
from rest_framework import serializers
from accounts.api.v1.serializers import AuthorSerializer




class TaskSerializer(serializers.ModelSerializer):
    user = AuthorSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_date','created_at','update_at','user']


class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']