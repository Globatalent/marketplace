from rest_framework import permissions


class OnlyOwnerUpdates(permissions.BasePermission):
    """Only allows updates to the owner (user field) of the model, and not creation."""

    def has_permission(self, request, view):
        if request.method in ('POST', ):
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'PATCH'):
            return obj.user == request.user
        return True


class OnlyAthletes(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return hasattr(request.user, 'athlete')
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'PATCH'):
            return obj.user == request.user
        return True
