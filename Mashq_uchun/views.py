from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def salomlash(request):
    return render(request, "salomlash.html")

def bosh(request):
    return HttpResponse("Bosh sahifaga xush kelibsiz")

def oquvchilar(request):
    s = ["Shukurillo", "Ramziddin", "Abdumajid"]
    return render(request, "oquvchilar.html", {"students" : s})

def oquvchi(request, ism):
    s = ["Shukurillo", "Ramziddin", "Abdumajid"]
    s.remove(ism)
    return render(request, "oquvchi.html", {"students": s})





