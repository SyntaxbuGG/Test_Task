from drf_spectacular.utils import extend_schema_field

from ...models import Task
from rest_framework import serializers
from accounts.api.v1.serializers import AuthorSerializer




class TaskSerializer(serializers.ModelSerializer):
    user = AuthorSerializer(read_only=True)

    @extend_schema_field(serializers.ChoiceField(choices=Task.STATUS_CHOICES))
    def get_status(self, obj):
        return obj.status
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_date','created_at','update_at','user']


class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']