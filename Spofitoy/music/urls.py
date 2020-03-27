from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name ='index'),
    path('top_songs', views.TopSongs.as_view(), name ='top_songs'),
    path('artist/', views.Artists.as_view(), name = 'artist'),
    path('artist/create_artist/', views.CreateArtist.as_view(), name = 'create_artist'),
]