from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.encoding import uri_to_iri
from .models import *
from django.views.generic import *
from .forms import *
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import Profile


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
        context['advertise'] = advertise.objects.all()
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertise_list'] = advertise.objects.all()
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comment_set.filter(is_active=True)
        context['category'] = Category.objects.all()
        return context


class Comment(SingleObjectMixin, FormView):
    template_name = 'ad_detail.html'
    form_class = CommentForm
    model = advertise

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        new_form = form.save(commit=False)
        new_form.advertise = self.object
        new_form.save()
        messages.info(self.request, message="نظر شما با موفقیت ثبت شد، در اولین فرصت بررسی میکنیم.")
        return super(Comment, self).form_valid(form)

    def get_success_url(self):
        return reverse('advertise-detail', kwargs={'slug': self.object.slug})

    def get_object(self, **kwargs):
        slug = self.kwargs.get('slug')
        return get_object_or_404(advertise, slug=uri_to_iri(slug))


class AdsandComment(View):
    def get(self, requset, *args, **kwargs):
        view = AdvertiseDisplay.as_view()
        return view(requset, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = Comment.as_view()
        return view(request, *args, **kwargs)


class CreateAdvertise(LoginRequiredMixin, CreateView):
    model = advertise
    login_url = '/account/sign_in/'
    redirect_field_name = 'home'
    template_name = 'createad.html'
    form_class = CreateAdvertise


class AdvertiseList(ListView):
    model = advertise
    template_name = 'advertiselist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertise'] = advertise.objects.all()
        return context


class DeleteAdvertise(LoginRequiredMixin, DeleteView):
    template_name = 'deleteadvertise.html'
    login_url = '/account/sign_in/'
    redirect_field_name = 'home'

    def get_object(self, **kwargs):
        slug = self.kwargs.get('slug')
        return get_object_or_404(advertise, slug=uri_to_iri(slug))

    def get_success_url(self):
        return reverse('account:dashboard')


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
