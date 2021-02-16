from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="maps-home"),
    path('about/', views.about, name="maps-about")
]