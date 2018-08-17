from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet

from marketplace.supporters.api.v1.permissions import CreateUpdateOnlySupporters
from marketplace.supporters.api.v1.serializers import AlertSerializer
from marketplace.supporters.models import Alert


class AlertViewSet(CreateModelMixin,
                   UpdateModelMixin,
                   DestroyModelMixin,
                   ReadOnlyModelViewSet):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
    permissions_classes = [
        CreateUpdateOnlySupporters
    ]

    def get_queryset(self):
        return Alert.objects.filter(supporter__exact=self.request.user.supporter.id)

    def perform_create(self, serializer):
        return serializer.save(supporter=self.request.user.supporter)

