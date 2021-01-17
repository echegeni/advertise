from django.shortcuts import render
from .models import *
from django.views.generic import *


# Create your views here.

class HomeView(TemplateView):
    model = advertise
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = city.objects.all()
        context['category'] = Category.objects.all()
        return context


# city model views

class CityList(ListView):
    model = city
    template_name = "City/CityList.html"


# category model views
class Category_List(ListView):
    model = Category
    template_name = "Category/CategoryList.html"
