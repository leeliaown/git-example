from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World!")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_date = datetime.now()
    my_content = {
        "my_text": "This is about us",
        "my_date": my_date,
        "number": 23,
        "my_list": ['abc', 'lee', 'fgr']

    }
    return render(request, "about.html", my_content)
