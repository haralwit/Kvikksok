from django.shortcuts import render
from .models import Post, Postnummer, Kvikkleire
from django.core import serializers
from .forms import PostForm


def home(request):
    data = serializers.serialize("geojson", Post.objects.all())
    mapbox_access_token = 'pk.eyJ1Ijoic2t1cDI1MDYiLCJhIjoiY2trMnJidzJkMTNyaDJvdDdrMmpuODR1biJ9.UozLDX9kk8-CC4irjB1nNQ'
    return render(request, 'maps\home.html', 
                  { 'mapbox_access_token': mapbox_access_token,
                  'postnummers': Postnummer.objects.values("geom").all(),
                  'posts' : data}
                  )

def savePost(request):
    print('1')
    if request.method == 'POST':
        print('2')
        form = PostForm(request.POST)
        if form.is_valid():
            print('3')
            form.save()
            title = form.cleaned_data.get('username')
            messages.success(request, f"{title}-Marker is saved")
            return redirect('maps-about', )


def about(request):
    return render(request, 'maps/about.html', {'title': 'About Us'})

def messages(request):
    context = {
        'posts' : Post.objects.all(),
    }
    return render(request, 'maps/messages.html', context)