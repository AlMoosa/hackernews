from django.shortcuts import render
from django.http import HttpResponse
from hackernews.forms import UserSignUpForm, UpdateForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from hackernews.models import Profile , User, News
from hackernews.scraping import Parser
from django.core.paginator import Paginator
from django.db.models import Q



def index(request):
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
            News.objects.create(
                title=title, link=link
            )
    
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






    

