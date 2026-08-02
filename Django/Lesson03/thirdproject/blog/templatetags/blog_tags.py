from django import template
from blog.models import Post, Category

register = template.Library()

@register.simple_tag(name="totalpost")
def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name="posts")
def function2():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value):
    return value[:100]

@register.inclusion_tag("blog/popular-post.html")
def popularposts():
    posts = Post.objects.filter(status=1).order_by("-published_date")[:3]
    return {"posts": posts}

@register.inclusion_tag("blog/post-categories.html")
def post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {"category": cat_dict}