from django.shortcuts import render
from .models import Post

# Create your views here.
def blog_home(request):
    posts = Post.objects.all().filter(status=1)
    return render(request, "blog/blog-home.html", {"posts": posts})

def blog_single(request, pid):
    post = Post.objects.get(id=pid, status=1)
    next_post = Post.objects.filter(id__gt=pid, status=1).order_by("id").first()
    privious_post = Post.objects.filter(id__lt=pid, status=1).order_by("id").first()
    context = {"post": post, "next_post": next_post, "privious_post": privious_post}
    return render(request, "blog/blog-single.html", context)