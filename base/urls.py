from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="homepage"),
    path('about/', views.about, name="kuhusu"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
    path('news/', views.news, name="news"),
    path('services/', views.services, name="services"),
]