from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from account.models import Profile

class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'input100', 'name': 'username', 'placeholder': 'ایمیل'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input100', 'name': 'username', 'placeholder': 'نام کاربری'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'name': 'pass', 'placeholder': 'رمز عبور'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'name': 'pass', 'placeholder': 'تکرار رمز عبور'}))

    class Meta:
        model = Profile
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
        labels = {
            'username': 'نام کاربری',
            'email': 'ایمیل',
        }
        help_texts = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }
        '''error_messages = {
            'password1': {
                'max_length': "This mmmmm writer's name is too long.",
            },
        }'''


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input100', 'name': 'username', 'placeholder': 'ایمیل'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'name': 'pass', 'placeholder': 'رمز عبور'}))


class RegisterForm22(UserCreationForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'input100', 'name': 'username', 'placeholder': 'ایمیل'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input100', 'name': 'username', 'placeholder': 'نام کاربری'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'name': 'pass', 'placeholder': 'رمز عبور'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100', 'name': 'pass', 'placeholder': 'تکرار رمز عبور'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
