from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('city/<str:slug>/', City_List.as_view(), name='city-list'),
    path('category/<str:slug>/', Category_List.as_view(), name='category_list'),
    path('search/', Search_Detail.as_view(), name='search'),
    path('ad/add/', CreateAdvertise.as_view(), name='create_advertise'),
    path('ad/list/', AdvertiseList.as_view(), name='list_advertise'),
    path('ad/<str:slug>/', AdsandComment.as_view(), name='advertise-detail'),
    path('ad/<str:slug>/delete/', DeleteAdvertise.as_view(), name='advertise-delete')
]
