from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "base.html")


def about(request):
    return render(request, "pages/about.html")

def installation(request):
    return render(request, "pages/installation.html")
