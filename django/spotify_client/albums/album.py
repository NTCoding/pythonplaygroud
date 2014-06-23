from django.http import HttpResponse


def search(request):
    query = request.GET.get("query")
    return HttpResponse("Album search for: %s" % query)