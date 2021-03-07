from django.shortcuts import render
from .models import Post, Postnummer


def home(request):
    mapbox_access_token = 'pk.eyJ1Ijoic2t1cDI1MDYiLCJhIjoiY2trMnJidzJkMTNyaDJvdDdrMmpuODR1biJ9.UozLDX9kk8-CC4irjB1nNQ'
    return render(request, 'maps\home.html', 
                  { 'mapbox_access_token': mapbox_access_token,
                  'postnummers': Postnummer.objects.values("geom").all()})

def about(request):
    return render(request, 'maps/about.html', {'title': 'About Us'})

def messages(request):
    context = {
        'posts' : Post.objects.all(),
    }
    return render(request, 'maps/messages.html', context)