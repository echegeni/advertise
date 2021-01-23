from django.contrib import messages
from django.contrib.auth import (authenticate, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                       PasswordChangeForm)
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from app.models import advertise
from . import forms
from .models import Profile


def sign_in(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('home')  # TODO: go to profile
                    )
                else:
                    messages.error(
                        request,
                        "حساب کاربری غیرفعال شده است"
                    )
            else:
                messages.error(
                    request,
                    "نام کاربری یا رمزعبور نادرست است."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = forms.RegistrationForm()
    if request.method == 'POST':
        form = forms.RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "عضویت با موفقیت انجام شد در حال ورود به سایت"
            )
            return HttpResponseRedirect(reverse('home'))  # TODO: go to profile
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, "باموفقت خارج شدید.")
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile(request):
    """Display User Profile"""
    profile = request.user.profile
    ads = advertise.objects.filter(user=profile.user)
    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'ads': ads
    })

@login_required
def edit_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    form = forms.ProfileForm(instance=profile)

    if request.method == 'POST':
        form = forms.ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پروفایل با موفقیت بروزرسانی شد.")
            return HttpResponseRedirect(reverse('accounts:profile'))

    return render(request, 'accounts/edit_profile.html', {
        'form': form
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'رمز عبور با موفقیت بروزرسانی شد.')
            return HttpResponseRedirect(reverse('accounts:profile'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
