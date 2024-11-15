from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

dummy_posts = [
    {
        "slug": "dummy",
        "image": "angryAlpaca.jpg",
        "author": "Angry Alpaca",
        "date": date(2024, 11, 11),
        "title": "Dummy",
        "excerpt": "There's nothing like the shits you get when eating this national cuisine!",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque dicta eaque est sed similique tenetur vel
            voluptates! Aliquam corporis, doloribus eaque et, excepturi ipsum libero, minus nam nostrum ratione rerum!
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque dicta eaque est sed similique tenetur vel
            voluptates! Aliquam corporis, doloribus eaque et, excepturi ipsum libero, minus nam nostrum ratione rerum!
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque dicta eaque est sed similique tenetur vel
            voluptates! Aliquam corporis, doloribus eaque et, excepturi ipsum libero, minus nam nostrum ratione rerum!
        """
    },
    {
        "slug": "dummy1",
        "image": "angryAlpaca.jpg",
        "author": "Angry Alpaca",
        "date": date(2024, 11, 12),
        "title": "Dummy 2",
        "excerpt": "There's nothing like the shits you get when eating this national cuisine!",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque dicta eaque est sed similique tenetur vel
            voluptates! Aliquam corporis, doloribus eaque et, excepturi ipsum libero, minus nam nostrum ratione rerum!
        """
    },
    {
        "slug": "dummy2",
        "image": "angryAlpaca.jpg",
        "author": "Angry Alpaca",
        "date": date(2024, 11, 13),
        "title": "Dummy 3",
        "excerpt": "There's nothing like the shits you get when eating this national cuisine!",
        "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cumque dicta eaque est sed similique tenetur vel
            voluptates! Aliquam corporis, doloribus eaque et, excepturi ipsum libero, minus nam nostrum ratione rerum!
        """
    }
]


def index(request: HttpRequest):
    latest_posts = sorted(dummy_posts, key=lambda entry: entry["date"])[-3:]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request: HttpRequest):
    return render(request, "blog/posts.html", {
        "posts": dummy_posts
    })


def post(request: HttpRequest, slug: str):
    return render(request, "blog/post-detail.html", {
        "post": next(entry for entry in dummy_posts if entry["slug"] == slug)
    })
