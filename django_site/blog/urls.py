from django.urls import path

from .views import index, posts, post

urlpatterns = [
    path("", index, name="index"),
    path("posts", posts, name="posts"),
    path("post/<slug:slug>", post, name="post"),
]