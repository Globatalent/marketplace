from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from marketplace.purchases.api.v1.permissions import CantUpdateDelete
from marketplace.purchases.api.v1.serializers import (
    PurchaseSerializer,
    PurchaseReadSerializer,
)
from marketplace.purchases.models import Purchase


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated, CantUpdateDelete]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PurchaseReadSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
