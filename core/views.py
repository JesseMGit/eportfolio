from django.shortcuts import render

def aboutme(request):
    return render(request, "core/aboutme.html")

def screenprint(request):
    return render(request, "core/screenprint.html")

def blackbox(request):
    return render(request, "core/blackbox.html")

def geneticsdocumentary(request):
    return render(request, "core/geneticsdocumentary.html")

def augbio(request):
    return render(request, "core/augmentedbiography.html")

def yearbook2425(request):
    return render(request, "core/yearbook2425.html")