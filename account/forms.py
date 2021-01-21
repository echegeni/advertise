from . import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import *


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='نام کاربری', required=True,
                               widget=forms.EmailInput(
                                   attrs={'id': "atbdp-contact-name", 'class': "form-control mb-3", 'type': "text",
                                          'placeholder': "نام کاربری"})
                               )
    email = forms.EmailField(label='ایمیل', required=True,
                             widget=forms.EmailInput(
                                 attrs={'id': "atbdp-contact-name", 'class': "form-control mb-3", 'type': "email",
                                        'placeholder': "ایمیل"}))

    password1 = forms.CharField(label='گذرواژه', required=True,
                                widget=forms.PasswordInput(
                                    attrs={'id': "atbdp-contact-name", 'class': "form-control mb-3", 'type': "password",
                                           'placeholder': "گذرواژه"}))

    password2 = forms.CharField(label='تأیید گذرواژه', required=True,
                                widget=forms.PasswordInput(
                                    attrs={'id': "atbdp-contact-name", 'class': "form-control mb-3", 'type': "password",
                                           'placeholder': "برای تائید، رمز عبور قبلی را وارد کنید."}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='نام کاربری', required=True,
                               widget=forms.EmailInput(
                                   attrs={'id': "atbdp-contact-name", 'class': "form-control mb-3", 'type': "text",
                                          'placeholder': "نام کاربری"}))

    password = forms.CharField(label='گذرواژه', required=True,
                               widget=forms.PasswordInput(
                                   attrs={'id': "atbdp-contact-name", 'class': "form-control mb-3", 'type': "password",
                                          'placeholder': "گذرواژه"}))

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(
        attrs={'id': "title", 'class': "form-control", 'placeholder': "ایمیل"}))

    confirm_email = forms.EmailField(label='تایید ایمیل', widget=forms.EmailInput(
        attrs={'id': "title", 'class': "form-control", 'placeholder': "تایید ایمیل"}))

    bio = forms.CharField(label='درباره شما', widget=forms.Textarea(
        attrs={'id': "title", 'class': "form-control", 'placeholder': "درباره شما"}))

    name = forms.CharField(label='نام', widget=forms.TextInput(
        attrs={'id': "title", 'class': "form-control", 'placeholder': "نام"}))

    family = forms.CharField(label='نام خانوادگی', widget=forms.TextInput(
        attrs={'id': "title", 'class': "form-control", 'placeholder': "نام خانوادگی"}))

    website = forms.URLField(label='وب سایت', widget=forms.URLInput(
        attrs={'id': "title", 'class': "form-control", 'placeholder': "وب سایت"}))

    phone = forms.IntegerField(label='شماره تماس', widget=(
        forms.NumberInput(attrs={'id': "title", 'class': "form-control", 'placeholder': "شماره تماس"})))

    pic = forms.ImageField(label='تصویر', widget=forms.FileInput(
        attrs={'id': "listing_image_btn", 'class': "btn btn-outline-primary m-right-10", 'placeholder': "شماره تماس"}))

    class Meta:
        model = models.Profile
        fields = [
            'name',
            'family',
            'email',
            'pic',
            'bio',
            'website',
            'phone',
        ]

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        bio = cleaned_data.get("bio")

        if email != confirm_email:
            raise forms.ValidationError(
                "Emails must match!"
            )

        if len(bio) < 10:
            raise forms.ValidationError(
                "Bio must be 10 characters or longer!"
            )
