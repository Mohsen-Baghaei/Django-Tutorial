from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("home/", views.blog_home, name="home"),
    path("single/", views.blog_single, name="single"),
]
