from django.shortcuts import render
from django.views import View

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
        return render(request, self.template)