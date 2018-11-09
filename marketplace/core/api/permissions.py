from rest_framework import permissions

from marketplace.users.helpers import is_athlete


class OnlyAthletes(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return is_athlete(request.user)
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ("PUT", "PATCH", "DELETE"):
            return obj.athlete.user == request.user
        return True
