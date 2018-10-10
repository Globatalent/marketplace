from rest_framework import permissions


class CantUpdateDelete(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ('PUT', 'PATCH', 'DELETE'):
            return False
        return True
