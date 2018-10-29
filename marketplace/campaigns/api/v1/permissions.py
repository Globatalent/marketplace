from rest_framework import permissions


class OnlyOwnerUpdates(permissions.BasePermission):
    """Only allows updates to the owner (user field) of the model, and not creation."""

    def has_object_permission(self, request, view, obj):
        if request.method in ("PUT", "PATCH", "DELETE"):
            return obj.user == request.user
        return True


class OnlyCampaignOwnerUpdates(permissions.BasePermission):
    """Only allows updates to the owner (user field) of the model, and not creation."""

    def has_object_permission(self, request, view, obj):
        if request.method in ("PUT", "PATCH", "DELETE"):
            return obj.campaign.user == request.user
        return True


class IsAuthenticatedForFollow(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "follow":
            return request.user and request.user.is_authenticated
        return True


class IsAuthenticatedForCreate(permissions.BasePermission):
    """Authentication is needed for creation."""

    def has_permission(self, request, view):
        if request.method in ("POST",):
            return request.user and request.user.is_authenticated
        return True
