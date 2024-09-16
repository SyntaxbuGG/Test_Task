from rest_framework.permissions import BasePermission


class IsAuthenticatedForListandCreate(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'create']:
            return request.user and request.user.is_authenticated
        return True


class IsUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.user == request.user
        return True
