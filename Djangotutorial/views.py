from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello, Django!")


def template(request):
    context = {
        "pen": "intekma",
        "food": "nasi lemak",
    }
    return render(request, "index.html", context)
