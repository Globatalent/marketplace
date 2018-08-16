from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.conf.urls import include, url
from rest_framework.documentation import include_docs_urls
from django.utils.translation import ugettext_lazy as _


urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

# Django Admin, use {% url 'admin:index' %}
admin.site.site_header = _('Globatalent Admin')
urlpatterns += [
    path(settings.ADMIN_URL, admin.site.urls),
]

# API URLs
# Create a router and register our resources with it.
urlpatterns += [
    path(r'api/docs/', include_docs_urls(title='Globatalent Marketplace API Docs')),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/', include('config.router', namespace='api')),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
