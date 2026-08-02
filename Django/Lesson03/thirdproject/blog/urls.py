from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("home/", views.blog_home, name="home"),
    path("post-<int:pid>/", views.blog_single, name="single"),
    path("category/<str:cat_name>", views.blog_category, name="category"),
    path("test/", views.test, name="test"),
]
