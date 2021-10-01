from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("INDEX response from pages->views.py")
def about(response):
    return HttpResponse("About Us response from pages->views.py")