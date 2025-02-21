from django.shortcuts import render
from django.http import HttpResponse

def aboutme(request):
    return HttpResponse(request, "core/aboutme.html")

def screenprint(request):
    return render(request, "core/screenprint.html")

def blackbox(request):
    return render(request, "core/blackbox.html")