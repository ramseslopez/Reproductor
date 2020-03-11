from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('top_songs', views.TopSongs.as_view(), name='top_songs'),
]