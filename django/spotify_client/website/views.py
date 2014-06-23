from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def home(request):
    temp = loader.render_to_string("homepage.html")
    return HttpResponse(temp)



