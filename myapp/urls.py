from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('about', views.about, name='Aboutpage'),
    path('contact', views.contact, name='Contactpage'),
    path('icecream', views.ice_cream, name='ice_cream'),
    path('milkshake', views.milk_shake, name='milk_shake'),
    path('familycombo', views.family_combo, name='family_combo'),
    path('ice-cream/<int:pk>/', views.ice_cream_detail, name='ice_cream_detail'),
]
