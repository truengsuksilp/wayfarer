from django.urls import path
from .views import Home, ProfileDetail, ProfileUpdate

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', ProfileUpdate.as_view(), name='profile_update')
]