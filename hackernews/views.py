from django.shortcuts import render
from django.http import HttpResponse
from hackernews.forms import UserSignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from hackernews.models import Profile , User, News
# from hackernews.scraping import main



def index(request):
    news = News.objects.all()
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        link = request.POST.get('link')
        News.objects.create(
            title = title, body=body, link=link
        )
    return render(request, 'news.html', {"news": news})



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



    

