from django.urls import path

from marketplace.emails.views import PreviewEmailView

app_name = 'emails'
urlpatterns = [
    path('previews/', PreviewEmailView.as_view(), name='preview'),
]
