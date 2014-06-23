from django.http import HttpResponse
import requests
import json

def search(request):
    query = request.GET.get("query")
    spotify_url = "https://api.spotify.com/v1/search?q=" + query + "&type=album"
    response_json = requests.get(spotify_url).json()
    albums = [  __toAlbum(a) for a in response_json['albums']['items'] ]
    response = json.dumps({ "albums": albums })
    return HttpResponse(response, content_type="application/json")

def __toAlbum(album):
	return {
		"album" : {
		    "name": album['name'],
            "image": album['images'][0],
            "link": album['uri']
		}
	}