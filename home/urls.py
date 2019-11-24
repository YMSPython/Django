from django.contrib import admin
from django.urls import path, include


from . import views  # views içerisinde yer alan tüm sayfları getir.

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('reference/', views.reference, name='reference'),
]
