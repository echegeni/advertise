from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.encoding import uri_to_iri
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


class AdvertiseDisplay(DetailView):
    model = advertise
    template_name = 'ad_detail.html'

    def get_object(self, **kwargs):
        slug = self.kwargs.get('slug')
        return get_object_or_404(advertise, slug=uri_to_iri(slug))


# city model views

class City_List(ListView):
    model = advertise
    template_name = "City/CityList.html"

    def get_queryset(self):
        querysert = advertise.objects.filter(city__slug=uri_to_iri(self.kwargs.get('slug')))
        return querysert


# category model views
class Category_List(ListView):
    model = advertise
    template_name = "Category/CategoryList.html"

    def get_queryset(self):
        queryset = advertise.objects.filter(category__slug=uri_to_iri(self.kwargs.get('slug')))
        return queryset
