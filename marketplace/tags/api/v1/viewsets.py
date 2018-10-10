from rest_framework import viewsets

from marketplace.tags.api.v1.serializers import TagSerializer
from marketplace.tags.models import Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
