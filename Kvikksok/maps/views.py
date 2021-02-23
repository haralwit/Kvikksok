from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Sigrid',
        'title': 'Maps Post 1',
        'content': 'First Post Content!',
        'date_posted': 'Fabruary 21, 2021'

    }

]


def home(request):
    mapbox_access_token = 'pk.eyJ1Ijoic2t1cDI1MDYiLCJhIjoiY2trMnJidzJkMTNyaDJvdDdrMmpuODR1biJ9.UozLDX9kk8-CC4irjB1nNQ'
    return render(request, 'maps\home.html', 
                  { 'mapbox_access_token': mapbox_access_token })

def about(request):
    return render(request, 'maps/about.html', {'title': 'About Us'})

def messages(request):
    context = {
        'posts' : posts
    }
    return render(request, 'maps/messages.html', context)