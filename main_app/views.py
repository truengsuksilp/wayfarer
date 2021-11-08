from django.db.models.base import Model
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from main_app.models import Profile, Post, City

from datetime import datetime
# TODO Add Auth 

# import the class that will handle basic views
from django.views import View

# auth imports
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'

class ProfileDetail(DetailView):
    model = Profile
    template_name = "profile_detail.html"

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['name', 'current_city']
    template_name = "profile_update.html"
    def get_success_url(self):
        return reverse("profile_detail", kwargs={'pk': self.object.pk})

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.filter(user = Profile)
        return context

# Signup view
class Signup(View):
    def get(self, request, **kwargs):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        name = request.POST.get("name")
        city = request.POST.get("current_city")
        image = request.POST.get("profile_picture")
        
        
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(name=name, current_city=city, profile_picture=image, user=user)

            login(request, user)
            return redirect("profile_detail", pk=profile.pk)
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class CityDetail(DetailView):
    model = City
    template_name = "city_detail.html"
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['now'] = datetime.now()
        return context

class PostCreate(View):
    def post(self, request, pk):
        Post.objects.create(
            city = request.POST.get('post-city'),
            title = request.POST.get('post-title'),
            content = request.POST.get('post-content'),
        )

class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete_confirm.html"

    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.object.city.pk})

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = "post_create.html"
    success_url = "/"