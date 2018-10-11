from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from marketplace.campaigns.api.v1.filters import CampaignFilter
from marketplace.campaigns.api.v1.permissions import (
    OnlyOwnerUpdates,
    IsAuthenticatedForCreate,
    OnlyCampaignOwnerUpdates,
    IsAuthenticatedForFollow)
from marketplace.campaigns.api.v1.serializers import (
    CampaignSerializer,
    PictureSerializer,
    LinkSerializer,
    SportSerializer,
    RevenueSerializer,
    IncomeSerializer,
    RecommendationSerializer, ReadCampaignSerializer)
from marketplace.campaigns.models import Campaign, Picture, Link, Sport, Revenue, Income, Recommendation


class SportViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SportSerializer
    queryset = Sport.objects.all()


class PictureViewSet(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()
    permission_classes = [
        IsAuthenticated,
        OnlyCampaignOwnerUpdates,
    ]


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [
        IsAuthenticated,
        OnlyCampaignOwnerUpdates,
    ]


class RevenueViewSet(viewsets.ModelViewSet):
    serializer_class = RevenueSerializer
    queryset = Revenue.objects.all()
    permission_classes = [
        IsAuthenticated,
        OnlyCampaignOwnerUpdates,
    ]


class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = [
        IsAuthenticated,
        OnlyCampaignOwnerUpdates,
    ]


class RecommendationViewSet(viewsets.ModelViewSet):
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all()
    permission_classes = [
        IsAuthenticated,
        OnlyCampaignOwnerUpdates,
    ]


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [
        IsAuthenticatedForCreate,
        IsAuthenticatedForFollow,
        OnlyOwnerUpdates,
    ]
    filterset_class = CampaignFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadCampaignSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @action(methods=['post'], detail=True)
    def follow(self, request, **kwargs):
        campaign = self.get_object()
        return Response(data={'following': request.user.follow(campaign)})
