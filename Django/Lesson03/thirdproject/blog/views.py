from django.shortcuts import render
from .models import Post

# Create your views here.
def test(request):
    return render(request, "blog/test.html")

def blog_home(request, **kwargs):
    posts = Post.objects.all().filter(status=1)
    if kwargs.get("cat_name") != None:
        posts = posts.filter(category__name=kwargs["cat_name"])
    if kwargs.get("author_username") != None:
        posts = posts.filter(author__username = kwargs["author_username"])
    return render(request, "blog/blog-home.html", {"posts": posts})

def blog_single(request, pid):
    post = Post.objects.get(id=pid, status=1)
    next_post = Post.objects.filter(id__gt=pid, status=1).order_by("id").first()
    privious_post = Post.objects.filter(id__lt=pid, status=1).order_by("id").first()
    context = {"post": post, "next_post": next_post, "privious_post": privious_post}
    return render(request, "blog/blog-single.html", context)

def blog_search(request):
    # print(request.__dict__)
    posts = Post.objects.filter(status=1)
    if s := request.GET.get("s"):
        posts = posts.filter(content__contains=s)

    context = {"posts": posts}

    return render(request, "blog/blog-home.html", context)