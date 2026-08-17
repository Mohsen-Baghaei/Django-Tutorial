from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def blog_home(request, **kwargs):
    posts = Post.objects.filter(status=1)

    if kwargs.get("cat_name") != None:
        posts = posts.filter(category__name=kwargs["cat_namw"])

    if kwargs.get("author_username") != None:
        posts = posts.filter(author__username=kwargs["author_username"])

    posts = Paginator(posts, 3)

    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    return render(request, "blog/blog-home.html", {"posts": posts})

def blog_single(request, pid):
    post = Post.objects.get(id=pid, status=1)
    next_post = Post.objects.filter(id__gt=pid, status=1).order_by("id").first()
    privious_post = Post.objects.filter(id__lt=pid, status=1).order_by("id").first()

    context = {"post": post, "next_post":next_post, "privious_post":privious_post}

    return render(request, "blog/blog-single.html", context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if s:= request.GET.get("s"):
        posts = posts.filter(title__contains=s)
    return render(request, "blog/blog-home.html", {"posts": posts})