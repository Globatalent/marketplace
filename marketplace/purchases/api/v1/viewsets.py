from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from marketplace.purchases.api.v1.permissions import CanCreatePurchase, CantUpdateDelete
from marketplace.purchases.api.v1.serializers import PurchaseSerializer, PurchaseReadSerializer
from marketplace.purchases.models import Purchase
from marketplace.users.helpers import is_supporter, is_athlete


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [
        IsAuthenticated,
        CantUpdateDelete,
        CanCreatePurchase,
    ]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PurchaseReadSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()
        if is_supporter(self.request.user):
            return queryset.filter(supporter__user=self.request.user)
        elif is_athlete(self.request.user):
            return queryset.filter(token__athlete__user=self.request.user)
        return queryset.none()

    def perform_create(self, serializer):
        return serializer.save(supporter=self.request.user.supporter)

