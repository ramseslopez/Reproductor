from django.shortcuts import render
from django.views import View
from .models import Song

# Create your views here.
def index(request):
    return render(request, 'music/index.html')

def top_songs(request):
    return render(request, 'music/top_songs.html')

class Index(View):

    template = "music/index.html"

    def get(self, request):
        return render(request, self.template)

class TopSongs(View):

    template =  "music/top_songs.html"

    def get(self, request):
        """GET method."""
        songs = Song.objects.all()
        to_play_id = request.GET.get("to_play", 1)
        songs_to_play = Song.objects.filter(id = to_play_id)
        if songs_to_play.count() == 0:
            to_play = Song.objects.first()
        else:
            to_play = songs_to_play.first()

        context = {"songs": songs, "to_play": to_play}
        return render(request, self.template, context)