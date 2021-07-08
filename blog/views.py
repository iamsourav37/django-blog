from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

post = [
    {
        "author": "Sourav",
        "title": "Why Django",
        "content": "django is very powerful framework based on Python",
        "date_post": "July 08, 2021"
    },
    {
        "author": "Sourav",
        "title": "Why React",
        "content": "React is very popular, single page application javascript library",
        "date_post": "July 08, 2021"
    },
]


def home(request):
    context = {
        "title": "Home",
        "home_active": True,
        "posts": post
    }
    return render(request, "blog/home.html", context)


def about(request):
    context = {
        "title": "About",
        "about_active": True,
    }
    return render(request, "blog/about.html", context)
