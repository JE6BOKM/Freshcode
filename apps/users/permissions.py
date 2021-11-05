from rest_framework import permissions

from .models import UserRole


class IsUserOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user


class IsAdmin(permissions.BasePermission):
    """
    Only allowed to admin
    """

    message = "ADMIN ONLY ALLOWED"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role == UserRole.ADMIN:
                return True
            return False
        else:
            return False
