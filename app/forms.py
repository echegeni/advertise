from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control", 'id': 'review_content', 'name': "content"}))

    class Meta:
        model = Comment
        fields = ['comment']
