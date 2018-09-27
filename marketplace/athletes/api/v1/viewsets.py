from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from marketplace.athletes.api.v1.filters import AthleteFilter, ReviewFilter, LinkFilter, PictureFilter
from marketplace.athletes.api.v1.permissions import OnlyOwnerUpdates, OnlyAthleteOwnerUpdates
from marketplace.athletes.api.v1.serializers import PictureSerializer, LinkSerializer, AthleteSerializer, \
    ReviewSerializer
from marketplace.athletes.models import Picture, Link, Athlete, Review
from marketplace.core.api.permissions import OnlyAthletes
from marketplace.supporters.models import Supporter
from marketplace.users.helpers import is_supporter


class PictureViewSet(ModelViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()
    permission_classes = [
        IsAuthenticated,
        OnlyAthletes,
        OnlyAthleteOwnerUpdates,
    ]
    filter_class = PictureFilter

    def perform_create(self, serializer):
        return serializer.save(athlete=self.request.user.athlete)


class LinkViewSet(ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [
        IsAuthenticated,
        OnlyAthletes,
        OnlyAthleteOwnerUpdates,
    ]
    filter_class = LinkFilter

    def perform_create(self, serializer):
        return serializer.save(athlete=self.request.user.athlete)


class AthleteViewSet(ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [
        OnlyOwnerUpdates
    ]
    filter_class = AthleteFilter

    @action(methods=['post'], detail=True)
    def follow(self, request, **kwargs):
        if not is_supporter(request.user):
            raise PermissionDenied
        athlete = self.get_object()
        supporter = Supporter.objects.get(id=request.user.supporter.id)
        return Response(data={'following': supporter.follow(athlete)})


class ReviewViewSet(ReadOnlyModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [
        IsAuthenticated,
        OnlyAthletes,
    ]
    filter_class = ReviewFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(athlete__user=self.request.user)

