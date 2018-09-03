from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from marketplace.tokens.api.v1.filters import TokenFilter
from marketplace.tokens.api.v1.serializers import TokenSerializer
from marketplace.tokens.models import Token


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    filter_class = TokenFilter

    def perform_create(self, serializer):
        return serializer.save(athlete=self.request.user.athlete)
