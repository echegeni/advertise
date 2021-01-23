from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'id': 'review_content', 'name': "content"}))

    class Meta:
        model = Comment
        fields = ['comment']


class CreateAdvertise(forms.ModelForm):
    slug = forms.CharField(label='آدرس آگهی', widget=forms.TextInput(
        attrs={'id': "title", 'class': "form-control", 'placeholder': "آدرس دلخواه شما برای آگهی"}))

    title = forms.CharField(label='عنوان', widget=forms.TextInput(
        attrs={'id': "title", 'class': "form-control", 'placeholder': "عنوان"}))

    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(
        attrs={'id': "title", 'class': "form-control", 'placeholder': "ایمیل"}))

    content = forms.CharField(label='درباره آگهی', widget=forms.Textarea(
        attrs={'id': "title", 'class': "form-control", 'placeholder': "درباره آگهی"}))

    pic = forms.ImageField(label='تصویر', widget=forms.FileInput(
        attrs={'id': "listing_image_btn", 'class': "btn btn-outline-primary m-right-10", 'placeholder': "تصویر"}))

    video = forms.ImageField(label='ویدئو آگهی شما', required=False, widget=forms.FileInput(
        attrs={'id': "listing_image_btn", 'class': "btn btn-outline-primary m-right-10", 'placeholder': "ویدئو"}))

    address = forms.CharField(label='آدرس', widget=forms.TextInput(
        attrs={'id': "title", 'class': "form-control", 'placeholder': "آدرس"}))

    phone = forms.IntegerField(label='شماره تماس', widget=(
        forms.NumberInput(attrs={'id': "title", 'class': "form-control", 'placeholder': "شماره تماس"})))

    price = forms.IntegerField(label='قیمت', widget=(
        forms.NumberInput(attrs={'id': "title", 'class': "form-control", 'placeholder': "قیمت"})))

    is_active_comment = forms.BooleanField(label="فعال کردن نظرات", required=False, widget=(
        forms.CheckboxInput()))

    city = forms.ChoiceField.widget(
        attrs={'id': "select2-ad_categroy-container", 'class': "form-select2-selection__rendered",
               'placeholder': "قیمت"})

    class Meta:
        model = advertise
        fields = [
            'slug',
            'title',
            'content',
            'city',
            'price',
            'category',
            'pic',
            'image_gallery',
            'phone',
            'email',
            'address',
            'video',
            'is_active_comment'
        ]
