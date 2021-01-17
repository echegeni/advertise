from django.shortcuts import render
from .models import *
from django.views.generic import *


# Create your views here.

class HomeView(TemplateView):
    model = advertise
    template_name = 'home.html'
