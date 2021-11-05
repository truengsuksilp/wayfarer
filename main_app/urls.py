from django.urls import path, include
from . import views





from .views import Home, Profile, Post, ProfileDetail, ProfileUpdate


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile'),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', ProfileUpdate.as_view(), name='profile_update'),
    path('profile/<int:profile_pk>/posts/<int:pk>/', Post.as_view(), name='post_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]