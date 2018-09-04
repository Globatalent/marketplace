from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from marketplace.supporters.api.v1.permissions import CreateUpdateOnlySupporters, OnlyOwnerUpdates
from marketplace.supporters.api.v1.serializers import AlertSerializer, SupporterSerializer
from marketplace.supporters.models import Alert, Supporter
from marketplace.users.helpers import is_supporter


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
        queryset = super().get_queryset()
        if is_supporter(self.request.user):
            return queryset.filter(supporter__user=self.request.user)
        return queryset.none()

    def perform_create(self, serializer):
        return serializer.save(supporter=self.request.user.supporter)


class SupporterViewSet(ModelViewSet):
    queryset = Supporter.objects.all()
    serializer_class = SupporterSerializer
    permission_classes = [
        IsAuthenticated,
        OnlyOwnerUpdates
    ]
