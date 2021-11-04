from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
# TODO Add Models
# TODO Add Auth 

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'