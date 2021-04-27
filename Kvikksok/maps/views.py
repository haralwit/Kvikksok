from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Postnummer, Kvikkleire
from django.contrib.auth.models import User 
from django.core import serializers
from django.contrib.gis.geos import Point


def home(request):
    data = serializers.serialize("geojson", Post.objects.all())
    mapbox_access_token = 'pk.eyJ1Ijoic2t1cDI1MDYiLCJhIjoiY2trMnJidzJkMTNyaDJvdDdrMmpuODR1biJ9.UozLDX9kk8-CC4irjB1nNQ'
    return render(request, 'maps/home.html', 
                  { 'mapbox_access_token': mapbox_access_token,
                  'postnummers': Postnummer.objects.values("geom").all(),
                  'posts' : data}
                  )

def savePost(request):
    if request.method == 'POST' and request.user.is_authenticated:
        title = request.POST['title']
        msg = request.POST.get('msg', "none")
        latitude = request.POST.get('latitude', "none")
        longitude = request.POST.get('longitude', "none")
        user = request.user
        markerlocation = Point(float(longitude), float(latitude), srid=4326)
        marker = Post(title=title, content=msg, author = user, geom = markerlocation)
        marker.save()
        return HttpResponse('request passes')

def about(request):
    return render(request, 'maps/about.html', {'title': 'About Us'})

def messages(request):
    context = {
        'posts' : Post.objects.all(),
    }
    return render(request, 'maps/messages.html', context)
