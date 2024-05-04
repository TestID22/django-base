from django.views.generic import ListView
from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        "title" : "vitalii test"
    }
    return  render(request, "posts/index.html", context)
