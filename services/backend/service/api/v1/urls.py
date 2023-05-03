from django.urls import path, include
from django.conf import settings
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .user import urlpatterns as user_urls
from .rooms import urlpatterns as rooms_urls
from .rent import urlpatterns as rent_urls


_urlpatterns = [
    path('user/', include(user_urls)),
    path('room/', include(rooms_urls)),
    path('rent/', include(rent_urls)),
]


schema_view = get_schema_view(
    openapi.Info(
        title=settings.PROJECT_NAME,
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=_urlpatterns,
)

urlpatterns = _urlpatterns + [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]
