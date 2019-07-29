from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework.permissions import IsAuthenticated

from hackernews.forms import UserSignUpForm, UpdateForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
from hackernews.models import Profile , User, News, Comment
from hackernews.scraping import Parser
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework import generics, status
from hackernews.serializers import NewsSerializer, CommentSerializer, CommentCreateSerializer
from hackernews.paginator import HackerNewsViewPagination

def main(request):
    return render(request, 'main.html', {})


def index(request):
    search_query = request.GET.get('search','')

    if search_query:
        news = News.objects.filter(Q(title__icontains=search_query)| Q(link__icontains=search_query))
    else:
        news = News.objects.all()
    paginator = Paginator(news, 10)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        previous_url = '?page={}'.format(page.previous_page_number())
    else:
        previous_url=''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''



    a = Parser()
    a.get_all_links()
    news = News.objects.all()
    if request.method == "POST":
        for i,lk in enumerate(a.link):
            title = a.title[i]
            link = a.link[i]
            try:
                if News.objects.filter(title=title, link=link).exists():
                    continue
                else:
                    News.objects.create(
                        title=title, link=link
                    )
            except:
                print("False")
    
    context = {
        'page_object':page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'previous_url': previous_url,
    }
    return render(request, 'news.html', context)

class NewsDetailView(DetailView):
    model = News
    template_name = "news_detail.html"
    context_object_name = "news_detail"

class NewsUpdateView(UpdateView):
    model = News
    form_class = UpdateForm
    template_name = "news_edit.html"
    context_object_name = "news_edit"


class SignUp(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(ListView):
    queryset = Profile.objects.all()
    template_name = "registration/profile.html"


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "registration/profile_detail.html"
    context_object_name = "profile"

class NewsDeleteView(DeleteView):
    model=News
    template_name='news_delete.html'
    context_object_name='news_delete'
    success_url = reverse_lazy('index')


def add_comment_to_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


class NewsLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id_ =self.kwargs.get("pk")
        obj=get_object_or_404(News, pk=id_)
        url_= "/"
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_


class NewsListViewSerializer(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = HackerNewsViewPagination


class NewsDetailViewSerializer(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsUpdateViewSerializer(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDeleteViewSerializer(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CommentListViewSerializer(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateViewSerializer(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



