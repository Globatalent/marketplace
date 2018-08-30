from rest_framework import permissions

from marketplace.users.helpers import is_supporter


class CantUpdateDelete(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'PATCH', 'DELETE'):
            return False
        return True


class CanCreatePurchase(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ('POST', ):
            return is_supporter(request.user)
        return True

