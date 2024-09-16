from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiParameter
from rest_framework import viewsets, filters
from rest_framework.exceptions import PermissionDenied

from .serializers import TaskSerializer
from ... import models
from . import serializers
from . import permissions


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.IsAuthenticatedForListandCreate, permissions.IsUserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['status', 'due_date']

    @extend_schema(
        summary='List all tasks',
        description='Retrieve a list of all tasks.',
        responses={200: TaskSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary='Create a new task',
        description='Create a new task with the provided data.',
        request=TaskSerializer,
        responses={201: TaskSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary='Retrieve a specific task',
        description='Retrieve details of a specific task by its ID.',
        responses={200: TaskSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary='Update a task',
        description='Update an existing task with the provided data.',
        request=TaskSerializer,
        responses={200: TaskSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary='Partially update a task',
        description='Partially update an existing task with the provided data. Only fields included in the request will be updated.',
        request=TaskSerializer,
        responses={200: TaskSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary='Delete a task',
        description='Delete a task by its ID.',
        responses={204: None}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.TaskSerializer
        return serializers.TaskCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        def perform_update(self, serializer):
            if self.request.user != serializer.instance.user:
                raise PermissionDenied("You do not have permission to edit this task.")
            serializer.save()

    def perform_destroy(self, instance):

        if self.request.user != instance.user:
            raise PermissionDenied("You do not have permission to delete this task.")
        instance.delete()
