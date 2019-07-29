from django.urls import path
from hackernews.views import (
    index, SignUp, ProfileView,
    ProfileDetailView, NewsDetailView,
    NewsUpdateView, NewsDeleteView,
    add_comment_to_news,
    NewsLikeToggle, NewsListViewSerializer,
    NewsDetailViewSerializer, NewsUpdateViewSerializer, NewsDeleteViewSerializer, CommentListViewSerializer,
    CommentCreateViewSerializer,)


urlpatterns = [
    path('', index, name="index"),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile-list/',ProfileView.as_view(), name="profile"),
    path('profile-detail/<int:pk>/', ProfileDetailView.as_view(), name="profile-detail"),
    path("news_detail/<int:pk>/", NewsDetailView.as_view(), name="news_detail"),
    path("news_edit/<int:pk>/", NewsUpdateView.as_view(), name="news_edit"),
    path('news_delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/<int:pk>/comment/', add_comment_to_news, name='add_comment_to_news'),
    path('news_detail/<int:pk>/like/', NewsLikeToggle.as_view(), name='news_like'),
    path('news/', NewsListViewSerializer.as_view()),
    path('news/<int:pk>/', NewsDetailViewSerializer.as_view()),
    path('news/<int:pk>/update/', NewsUpdateViewSerializer.as_view()),
    path('news/<int:pk>/delete/', NewsDeleteViewSerializer.as_view()),
    path('comments/', CommentListViewSerializer.as_view()),
    path('comments/create/', CommentCreateViewSerializer.as_view()),

]