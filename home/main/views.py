from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to the home page!',
        'list': ['first', 'second', 'third', 'fourth', 'fifth', 'sixth'],
        'dict': {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5},
        'is_authenticated': False,
    }

    return render(request, "main/index.html", context)

def about(request):
    return HttpResponse("About Page")
