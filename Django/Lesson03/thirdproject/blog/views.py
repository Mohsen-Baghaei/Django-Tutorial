from django.shortcuts import render
from .models import Post

# Create your views here.
def test(request):
    return render(request, "blog/test.html")

def blog_home(request, cat_name=None):
    posts = Post.objects.all().filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    return render(request, "blog/blog-home.html", {"posts": posts})

def blog_single(request, pid):
    post = Post.objects.get(id=pid, status=1)
    next_post = Post.objects.filter(id__gt=pid, status=1).order_by("id").first()
    privious_post = Post.objects.filter(id__lt=pid, status=1).order_by("id").first()
    context = {"post": post, "next_post": next_post, "privious_post": privious_post}
    return render(request, "blog/blog-single.html", context)
