from django.contrib.auth import views as auth_views
from django.urls import path
from account import views
from .forms import *
urlpatterns = [
    path('register/', views.SignUp.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutUser.as_view(), name="logout"),
]