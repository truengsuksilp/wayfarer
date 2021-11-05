from django.urls import path
from . import views
from .views import Home, Profile, Post

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/<int:pk>/', Profile.as_view(), name='profile'),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('accounts/login/', views.Login.as_view(), name='login' ),
    path('profile/<int:pk>/', Profile.as_view(), name='profile_detail'),
    path('profile/<int:profile_pk>/posts/<int:pk>/', Post.as_view(), name='post_detail')
]