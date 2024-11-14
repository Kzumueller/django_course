from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request: HttpRequest):
    return render(request, "blog/index.html")

def posts(request: HttpRequest):
    pass

def post(request: HttpRequest, slug: str):
    pass