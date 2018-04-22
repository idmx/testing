from django.shortcuts import render
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ind/', views.index, name='index'),
    url(r'^$', views.site, name='site'),
]
# Create your views here.
