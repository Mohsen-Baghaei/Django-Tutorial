from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")

def about(request):
    return render(request, "anout.html")

def elements(request):
    return render(request, "elements.html")