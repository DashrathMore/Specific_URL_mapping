from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<marquee> <h1> family Is<i> Everything.........</h1></marquee>')


def second(request):
    return HttpResponse('<h1> I AM IRONMAN..... </h1>')