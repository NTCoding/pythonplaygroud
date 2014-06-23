from django.http import HttpResponse
import requests

def search(request):
    query = request.GET.get("query")
    spotify_url = "http://ws.spotify.com/search/1/album.json?q=" + query
    response = requests.get(spotify_url)
    return HttpResponse(response.text, content_type="application/json")