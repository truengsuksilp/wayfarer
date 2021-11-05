from django.urls import path
from . import views
from .views import Home, Profile, Post, ProfileDetail, ProfileUpdate

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('accounts/login/', views.Login.as_view(), name='login' ),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', ProfileUpdate.as_view(), name='profile_update'),
    path('profile/<int:profile_pk>/posts/<int:pk>/', Post.as_view(), name='post_detail')
]