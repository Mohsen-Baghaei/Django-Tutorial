from django.shortcuts import render
from django.views import View

def homepage(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog_home(request):
    return render(request, "blog_home.html")

def blog_single(request):
    return render(request, "blog_single.html")

def contact(request):
    return render(request, "contact.html")

def elements(request):
    return render(request, "elements.html")

def hotels(request):
    return render(request, "hotels.html")

def insurance(request):
    return render(request, "insurance.html")

def packages(request):
    return render(request, "packages.html")