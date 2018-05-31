from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet

from marketplace.actions.api.v1.serializers import NotificationSerializer
from marketplace.actions.models import Notification


class NotificationViewSet(UpdateModelMixin,
                          ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def get_queryset(self):
        return Notification.objects.filter(user_id=self.request.user.id)
