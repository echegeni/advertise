from django.db.models import Q
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
        context['favcity'] = city.objects.filter(fav=True)
        context['favcat'] = Category.objects.filter(fav=True)
        context['category'] = Category.objects.all()
        return context


class Search_Detail(ListView):
    model = advertise
    template_name = 'search_detail.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = advertise.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query) | Q(city__icontains=query)
        )
        return object_list


# city model views

class CityList(ListView):
    model = city
    template_name = "City/CityList.html"


# category model views
class Category_List(ListView):
    model = Category
    template_name = "Category/CategoryList.html"
