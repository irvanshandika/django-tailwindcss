from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    first_name = 'Muhammad Irvan'
    last_name = 'Shandika'

    context = {
        'first_name': first_name,
        'last_name': last_name,
    }
    return render(request, "base.html", context)
