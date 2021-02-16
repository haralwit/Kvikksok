from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Hello world bitches </h1>")

def about(request):
    return HttpResponse('<h1> This is a generic about page </h1>')

