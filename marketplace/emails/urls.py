from django.urls import path

from climatetrade.emails.views import PreviewEmailView

app_name = 'emails'
urlpatterns = [
    path('previews/', PreviewEmailView.as_view(), name='preview'),
]
