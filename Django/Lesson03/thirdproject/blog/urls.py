from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.blog_home, name="home"),
    path("post-<int:pid>/", views.blog_single, name="single")
]
