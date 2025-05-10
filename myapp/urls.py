from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('about', views.about, name='Aboutpage'),
    path('contact', views.contact, name='Contactpage'),
    path('service', views.service, name='Servicepage'),
]