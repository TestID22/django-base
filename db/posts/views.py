from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from .models import Post
from .forms import NameForm

def index(request):
    form = NameForm()
    if request.method == "POST":
        post = Post()
        form = NameForm(request.POST)
        print(form.data)
        post.post = form.data #TODO: fix incorrect recroding in the DB
        post.save()
    return  render(request, "posts/index.html", {"form": form }) #dont forget to add FORM for rendering
