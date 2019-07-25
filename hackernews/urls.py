from django.urls import path
from hackernews.views import index, SignUp, ProfileView, ProfileDetailView, NewsDetailView, NewsUpdateView, NewsDeleteView


urlpatterns = [
    path('', index, name="index"),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile-list/',ProfileView.as_view(), name="profile"),
    path('profile-detail/<int:pk>/', ProfileDetailView.as_view(), name="profile-detail"),
    path("news_detail/<int:pk>/", NewsDetailView.as_view(), name="news_detail"),
    path("news_edit/<int:pk>/", NewsUpdateView.as_view(), name="news_edit"),
    path('news_delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
]