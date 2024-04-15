from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/users/', include('auths.urls')),
    path('api/v2/prof/', include('profiles.urls')),
    path('managements/', include('managements.urls')),
    path('api/v4/pay/', include('tariffPayments.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
