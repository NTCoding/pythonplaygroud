from django.http import HttpResponse
import requests
import json

def search(request):
    query = request.GET.get("query")
    spotify_url = "http://ws.spotify.com/search/1/album.json?q=" + query
    response_json = requests.get(spotify_url).json()
    albums = [ a['name'] for a in response_json['albums'] ]
    response = json.dumps({ "albums": albums })
    return HttpResponse(response, content_type="application/json")