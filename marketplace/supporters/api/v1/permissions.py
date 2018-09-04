from rest_framework import permissions

from marketplace.users.helpers import is_supporter


class CreateUpdateOnlySupporters(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ('POST', 'PUT', 'PATCH'):
            return is_supporter(request.user)
        return True


class OnlyOwnerUpdates(permissions.BasePermission):
    """Only allows updates to the owner (user field) of the model, and not creation."""

    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'PATCH'):
            return obj.user == request.user
        return True
