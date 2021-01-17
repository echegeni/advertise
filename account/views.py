from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth import logout
from account import forms


# Create your views here.

class SignUp(CreateView):
    template_name = 'registration/signup.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LogoutUser(RedirectView):
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
