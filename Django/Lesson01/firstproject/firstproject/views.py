from django.shortcuts import render


def homepage(request):
    return render(request, "index.html")

def blog_home(request):
    return render(request, "blog-home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def elements(request):
    return render(request, "elements.html")

def blog_single(request):
    return render(request, "blog-single.html")