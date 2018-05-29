from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from marketplace.athletes.api.v1.serializers import PictureSerializer, LinkSerializer, AthleteSerializer
from marketplace.athletes.models import Picture, Link, Athlete
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action

from marketplace.supporters.models import Supporter


class PictureViewSet(ReadOnlyModelViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()


class LinkViewSet(ReadOnlyModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()


class AthleteViewSet(ReadOnlyModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer

    @action(methods=['post'], detail=True)
    def following(self, request, pk):
        if not (hasattr(request.user, 'supporter')):
            raise PermissionDenied

        athlete = Athlete.objects.get(id=pk)
        supporter = Supporter.objects.get(id=request.user.supporter.id)

        if Supporter.objects.filter(following__id=pk).count() == 1:
            supporter.following.remove(athlete)
            return Response(data={'following': False})

        supporter.following.add(athlete)
        return Response(data={'following': True})
