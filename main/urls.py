from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('hackernews/', include('hackernews.urls')),
    path('testing/', include('testing.urls')),
    path('admin/', admin.site.urls),
    path('hackernews/', include('django.contrib.auth.urls')),
]
