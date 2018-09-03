from django.conf.urls import include, url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from marketplace.actions.api.v1.viewsets import NotificationViewSet
from marketplace.athletes.api.v1.views import AthleteRegistrationView
from marketplace.athletes.api.v1.viewsets import AthleteViewSet, LinkViewSet, PictureViewSet, ReviewViewSet
from marketplace.purchases.api.v1.viewsets import PurchaseViewSet
from marketplace.supporters.api.v1.views import SupporterRegistrationView
from marketplace.supporters.api.v1.viewsets import AlertViewSet
from marketplace.tokens.api.v1.viewsets import TokenViewSet
from marketplace.users.api.v1.viewsets import UserViewSet, RestorePasswordViewSet, VerifyViewSet, \
    RequestRestoreCodeViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('athletes', AthleteViewSet, 'athletes')
router_v1.register('users', UserViewSet, 'users')
router_v1.register('links', LinkViewSet, 'links')
router_v1.register('pictures', PictureViewSet, 'pictures')
router_v1.register('alerts', AlertViewSet, 'alerts')
router_v1.register('notifications', NotificationViewSet, 'notifications')
router_v1.register('tokens', TokenViewSet, 'tokens')
router_v1.register('purchases', PurchaseViewSet, 'purchases')
router_v1.register('reviews', ReviewViewSet, 'reviews')
router_v1.register('request_restore_code', viewset=RequestRestoreCodeViewSet, base_name="request_restore_code")
router_v1.register('restore_password', viewset=RestorePasswordViewSet, base_name="restore_password")
router_v1.register('verify_email', viewset=VerifyViewSet, base_name="verify_email")

urlpatterns = [
    # Register
    url(r'^v1/register/athlete', AthleteRegistrationView.as_view(), name='register_athletes'),
    url(r'^v1/register/supporter', SupporterRegistrationView.as_view(), name='register_supporters'),
    # Obtaining a token. Security
    url(r'^v1/login/', obtain_jwt_token),
    url(r'^v1/refresh/', refresh_jwt_token),
    url(r'^v1/', include((router_v1.urls, 'v1'), namespace='v1'))
]
