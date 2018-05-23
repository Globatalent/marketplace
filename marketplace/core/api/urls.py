from __future__ import unicode_literals

from django.conf.urls import include, url
from rest_framework import routers
from marketplace.athletes.api.v1.viewsets import AthleteViewSet
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router_v1 = routers.DefaultRouter()

router_v1.register('athletes', AthleteViewSet, 'athletes')

app_name = 'api'
urlpatterns = [
    #url(r'^v1/register/$', InvestorRegistrationView.as_view(), name='register'),
    # Obtaining a token. Security
    url(r'^v1/login/', obtain_jwt_token),
    url(r'^v1/refresh/', refresh_jwt_token),
    url(r'^v1/', include((router_v1.urls, 'v1'), namespace='v1'))
]
