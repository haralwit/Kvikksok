from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'maps/home.html')

def about(request):
    return HttpResponse('<h1> This is a generic about page </h1>')

