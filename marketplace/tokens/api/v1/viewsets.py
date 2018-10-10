from rest_framework import viewsets

from marketplace.tokens.api.v1.filters import TokenFilter
from marketplace.tokens.api.v1.serializers import TokenSerializer
from marketplace.tokens.models import Token


class TokenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    filterset_class = TokenFilter
