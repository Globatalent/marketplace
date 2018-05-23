from rest_framework.viewsets import ReadOnlyModelViewSet
from marketplace.athletes.api.v1.serializers import PictureSerializer, LinkSerializer, AthleteSerializer
from marketplace.athletes.models import Picture, Link, Athlete


class PictureViewSet(ReadOnlyModelViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()


class LinkViewSet(ReadOnlyModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()


class AthleteViewSet(ReadOnlyModelViewSet):
    serializer_class = AthleteSerializer
    queryset = Athlete.objects.all()
