from django.urls import path
from . import views
from .views import Home, ProfileDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile'),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('accounts/login/', views.Login.as_view(), name='login' )
]