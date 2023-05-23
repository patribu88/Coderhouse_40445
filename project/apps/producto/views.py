from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def index(request: HttpRequest):
    return render(request, "producto/index.html")  # aplicación-archivo
