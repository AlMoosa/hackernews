from django.urls import path
from hackernews.views import index


urlpatterns = [
    path('', index, name="index"),
]