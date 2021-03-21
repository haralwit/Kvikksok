from django.shortcuts import render
from .models import Post, Postnummer, Kvikkleire
from django.core import serializers
data = serializers.serialize("geojson", Post.objects.all())

def home(request):
    mapbox_access_token = 'pk.eyJ1Ijoic2t1cDI1MDYiLCJhIjoiY2trMnJidzJkMTNyaDJvdDdrMmpuODR1biJ9.UozLDX9kk8-CC4irjB1nNQ'
    kvikkleire_data = serializers.serialize("geojson", Kvikkleire.objects.all())
    return render(request, 'maps\home.html', 
                  { 'mapbox_access_token': mapbox_access_token,
                  'postnummers': Postnummer.objects.values("geom").all(),
                  'posts' : data,
                  'kvikkleire': kvikkleire_data}
                  )

def about(request):
    return render(request, 'maps/about.html', {'title': 'About Us'})

def messages(request):
    context = {
        'posts' : Post.objects.all(),
    }
    return render(request, 'maps/messages.html', context)