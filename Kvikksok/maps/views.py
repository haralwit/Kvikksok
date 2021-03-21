from django.shortcuts import render
from django.core.serializers import serialize
from .models import Post, Postnummer

def home(request):
    mapbox_access_token = 'pk.eyJ1Ijoic2t1cDI1MDYiLCJhIjoiY2trMnJidzJkMTNyaDJvdDdrMmpuODR1biJ9.UozLDX9kk8-CC4irjB1nNQ'
    seralized_postnummer = serialize('geojson', Postnummer.objects.all())
    context = {
        'mapbox_access_token': mapbox_access_token,
        'serialized_postnummer': seralized_postnummer,
    }
    return render(request, 'maps\home.html', 
                  context)

def about(request):
    return render(request, 'maps/about.html', {'title': 'About Us'})

def messages(request):
    context = {
        'posts' : Post.objects.all(),
    }
    return render(request, 'maps/messages.html', context)