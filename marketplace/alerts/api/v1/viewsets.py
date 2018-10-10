from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from marketplace.alerts.api.v1.serializers import AlertSerializer
from marketplace.alerts.models import Alert


class AlertViewSet(viewsets.ModelViewSet):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
    permissions_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
