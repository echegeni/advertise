from django.urls import path , include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from account import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    # path('profile/', user_views.profile, name='profile'),
    path('profile/<str:username>', login_required(user_views.Profile.as_view()), name='user_profile'),
    path('editprofile/', user_views.edit_profile, name='edit_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]