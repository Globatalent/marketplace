from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from marketplace.athletes.api.v1.permissions import OnlyOwnerUpdates
from marketplace.core.api.permissions import OnlyAthletes
from marketplace.athletes.api.v1.serializers import PictureSerializer, LinkSerializer, AthleteSerializer
from marketplace.athletes.models import Picture, Link, Athlete
from marketplace.supporters.models import Supporter
from marketplace.users.helpers import is_supporter


class PictureViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()
    permission_classes = [
        OnlyAthletes
    ]

    def perform_create(self, serializer):
        return serializer.save(athlete=self.request.user.athlete)


class LinkViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [
        OnlyAthletes
    ]

    def perform_create(self, serializer):
        return serializer.save(athlete=self.request.user.athlete)


class AthleteViewSet(ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [
        OnlyOwnerUpdates
    ]

    @action(methods=['post'], detail=True)
    def follow(self, request, **kwargs):
        if not is_supporter(request.user):
            raise PermissionDenied
        athlete = self.get_object()
        supporter = Supporter.objects.get(id=request.user.supporter.id)
        return Response(data={'following': supporter.follow(athlete)})
