from django.shortcuts import render, get_list_or_404
from .models import Post

# Create your views here.
def blog_home(request):
    posts = Post.objects.all().filter(status = 1)
    return render(request, "blog/blog-home.html", {"posts": posts})

def blog_single(request, pid):
    post = Post.objects.get(id = pid, status = 1)
    next_post = Post.objects.filter(id__gt=pid, status=1).order_by("id").first()
    privious_post = Post.objects.filter(id__lt=pid, status=1).order_by("id").first() 
    # post = get_list_or_404(Post, pk=pid)
    return render(request, "blog/blog-single.html", {"post": post, "next_post": next_post, "privious_post": privious_post})