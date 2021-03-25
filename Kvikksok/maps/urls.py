from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name="maps-home"),
    path('about/', views.about, name="maps-about"),
    path('messages/', views.messages, name="maps-messages"),
    path('addMarker/', views.savePost, name='maps-addMarker')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
