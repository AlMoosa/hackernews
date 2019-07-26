from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from hackernews.views import main
from django.conf.urls.static import static

urlpatterns = [
    path('hackernews/', include('hackernews.urls')),
    path('testing/', include('testing.urls')),
    path('admin/', admin.site.urls),
    path('hackernews/', include('django.contrib.auth.urls')),
    path('', main , name="main"),
    path('api/v1/', include('rest_framework.urls')),
    path('api/v1/', include('hackernews.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
