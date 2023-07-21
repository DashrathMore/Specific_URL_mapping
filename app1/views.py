from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1> LOVE YOU 3000....')

def second(request):
    return HttpResponse('<marquee><h1> Avengers Ascemble.....')