from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Postnummer, Kvikkleire
from django.contrib.auth.models import User 
from django.core import serializers
from django.contrib.gis.geos import Point
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    data = serializers.serialize("geojson", Post.objects.all())
    mapbox_access_token = 'pk.eyJ1Ijoic2t1cDI1MDYiLCJhIjoiY2trMnJidzJkMTNyaDJvdDdrMmpuODR1biJ9.UozLDX9kk8-CC4irjB1nNQ'
    return render(request, 'maps\home.html', 
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

class PostListView(ListView):
    model = Post
    template_name = 'maps/messages.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'geom']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'geom']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = "/messages/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False