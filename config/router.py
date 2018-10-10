from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from marketplace.actions.api.v1.viewsets import NotificationViewSet
from marketplace.alerts.api.v1.viewsets import AlertViewSet
from marketplace.campaigns.api.v1.viewsets import CampaignViewSet, SportViewSet, RevenueViewSet, PictureViewSet, \
    LinkViewSet, IncomeViewSet, RecommendationViewSet
from marketplace.purchases.api.v1.viewsets import PurchaseViewSet
from marketplace.tokens.api.v1.viewsets import TokenViewSet
from marketplace.users.api.v1.viewsets import UserViewSet, RestorePasswordViewSet, VerifyViewSet, \
    RequestRestoreCodeViewSet, me

app_name = 'api_v1'

router_v1 = routers.DefaultRouter()
router_v1.register('request_restore_code', RequestRestoreCodeViewSet, "request_restore_code")
router_v1.register('restore_password', RestorePasswordViewSet, "restore_password")
router_v1.register('verify_email', VerifyViewSet, "verify_email")
router_v1.register('users', UserViewSet, 'users')
router_v1.register('sports', SportViewSet, 'sport')
router_v1.register('campaigns', CampaignViewSet, 'campaigns')
router_v1.register('pictures', PictureViewSet, 'pictures')
router_v1.register('links', LinkViewSet, 'links')
router_v1.register('revenues', RevenueViewSet, 'revenues')
router_v1.register('incomes', IncomeViewSet, 'incomes')
router_v1.register('recommendations', RecommendationViewSet, 'recommendations')
router_v1.register('alerts', AlertViewSet, 'alerts')
router_v1.register('notifications', NotificationViewSet, 'notifications')
router_v1.register('tokens', TokenViewSet, 'tokens')
router_v1.register('purchases', PurchaseViewSet, 'purchases')


urlpatterns = [
    path('users/me/', me, kwargs={'pk': 'me'}),
    path('', include(router_v1.urls)),
]
