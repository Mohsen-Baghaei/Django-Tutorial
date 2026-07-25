from django.shortcuts import render, get_list_or_404
from .models import Post

# Create your views here.
def blog_home(request):
    posts = Post.objects.all().filter(status = 1)
    return render(request, "blog/blog-home.html", {"posts": posts})

def blog_single(request, pid):
    # post = Post.objects.get(id = pid)
    post = get_list_or_404(Post, pk=pid)
    return render(request, "blog/blog-single.html", {"post": post})