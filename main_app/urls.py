from django.urls import path

from main_app.models import Post
from .views import Home, Profile, Post

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/<int:pk>/', Profile.as_view(), name='profile_detail'),
    path('profile/<int:pk>/posts/<int:post_pk>', Post.as_view(), name='post')
]