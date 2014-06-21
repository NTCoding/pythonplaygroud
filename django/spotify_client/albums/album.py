from django.http import HttpResponse


def album(request):
    return HttpResponse("Albums")