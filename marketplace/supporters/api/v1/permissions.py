from rest_framework import permissions

from users.helpers import is_supporter


class CreateUpdateOnlySupporters(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ('POST', 'PUT', 'PATCH'):
            return is_supporter(request.user)
        return True
