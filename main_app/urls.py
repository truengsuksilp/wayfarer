from django.urls import path, include
from . import views

from .views import Home, Post, ProfileDetail, ProfileUpdate, CityDetail


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', ProfileUpdate.as_view(), name='profile_update'),
    path('posts/<int:pk>/', Post.as_view(), name='post_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cities/<int:pk>/', CityDetail.as_view(), name="city_detail") 
]