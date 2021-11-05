from django.db.models.base import Model
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from main_app.models import Profile, Post, City
# TODO Add Models
# TODO Add Auth 

# import the class that will handle basic views
from django.views import View

# auth imports
from django.contrib.auth import login
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

class Post(DetailView):
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
            return redirect("profile", pk=profile.pk)
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

#Login View 
class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        context={"form": form}
        return render(request, "registration/login.html", context)
