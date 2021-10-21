# I have created this file - Aizaz

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params = {"Name": "Ali", "Place": "Mars"}
    return render(request, 'index.html', params)
    # return HttpResponse("Home")


def removePunc(request):
    return HttpResponse("Remove Punc")

def capfirst(request):
    return HttpResponse("Capitalize First")

def newlineremove(request):
    return HttpResponse("New Line Remove")

def spaceremove(request):
    return HttpResponse("Space Remove")

def charcount(request):
    return HttpResponse("Char Count")
