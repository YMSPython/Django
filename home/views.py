from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello Fıstıklı Baklava")

def index(request):
    return render(request, 'home/index.html')

def contact(request):
    return HttpResponse("İletişim Numarası")

def reference(request):
    return HttpResponse("Referans Sayfası")
