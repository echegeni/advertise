from . import models
from django import forms


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput())
    confirm_email = forms.EmailField(widget=forms.EmailInput())
    bio = forms.Textarea()

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
