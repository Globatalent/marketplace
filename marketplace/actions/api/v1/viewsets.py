from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from marketplace.actions.api.v1.filters import NotificationFilter
from marketplace.actions.api.v1.serializers import NotificationSerializer
from marketplace.actions.models import Notification


class NotificationViewSet(UpdateModelMixin, ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    filter_class = NotificationFilter

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    @action(detail=False)
    def count(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        content = {'count': queryset.count()}
        return Response(content)
