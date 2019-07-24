from django.urls import path
from hackernews.views import index, SignUp, ProfileView, ProfileDetailView


urlpatterns = [
    path('', index, name="index"),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile-list/',ProfileView.as_view(), name="profile"),
    path('profile-detail/<int:pk>/', ProfileDetailView.as_view(), name="profile-detail"),
]