from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Post
from .forms import NameForm

def index(request):
    form = NameForm()
    posts = Post.objects.all()
    if request.method == "POST":
        post = Post()
        form = NameForm(request.POST)
        print(form.data)
        post.post = form.data['your_task'] #TODO: fix incorrect recroding in the DB
        post.save()
    return  render(request, "posts/index.html", {"form": form, "posts": posts }) #dont forget to add FORM for rendering
