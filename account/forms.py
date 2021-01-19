from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(
            attrs={'class': "form-control mb-4", 'id': 'review_content', 'name': "content", 'placeholder': "نام کاربری"}))

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(
            attrs={'class': "form-control mb-4", 'id': 'review_content', 'name': "content", 'placeholder': "ایمیل"}))

    password1 = forms.CharField(
        label='گذرواژه',
        widget=forms.PasswordInput(
            attrs={'class': "form-control mb-4", 'id': 'review_content', 'name': "content", 'placeholder': "گذرواژه"}))

    password2 = forms.CharField(
        label='تایید گذرواژه',
        widget=forms.PasswordInput(
            attrs={'class': "form-control mb-4", 'id': 'review_content', 'name': "content", 'placeholder': "برای تائید، رمز عبور قبلی را وارد کنید."}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pic', 'name', 'bio']
