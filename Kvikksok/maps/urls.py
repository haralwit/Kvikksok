from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home, name="maps-home"),
    path('about/', views.about, name="maps-about"),
    path('messages/', views.messages, name="maps-messages")
]