from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from main_app.models import Profile, Post, City
# TODO Add Models

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class Profile(DetailView):
    model = Profile
    template_name = "profile_detail.html"

    def get_context(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.filter(user = Profile)
        return context

