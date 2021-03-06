from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name="maps-home"),
    path('about/', views.about, name="maps-about"),
    path('messages/', views.PostListView.as_view(), name="maps-messages"),
    path('messages/<int:pk>/', views.PostDetailView.as_view(), name="maps-messages-detail"),
    path('messages/new/', views.PostCreateView.as_view(), name="maps-messages-create"),
    path('messages/<int:pk>/update/', views.PostUpdateView.as_view(), name="maps-messages-update"),
    path('messages/<int:pk>/delete/', views.PostDeleteView.as_view(), name="maps-messages-delete"),
    path('addMarker/', views.savePost, name='maps-addMarker')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
