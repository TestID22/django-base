from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .models import Post
from .forms import NameForm, EmailMessageForm

def index(request):
    form = NameForm()
    email_message_form = EmailMessageForm()
    posts = Post.objects.all().order_by('-id')
    if request.method == "POST":
        post = Post()
        form = NameForm(request.POST)
        email_message_form = EmailMessageForm(request.POST)
        print(email_message_form.data)
        post.post = form.data['your_task']
        post.save()
        return redirect("/")
    return render(request, "posts/index.html", {"form": form, "posts": posts , "email_message_form": email_message_form}) #dont forget to add FORM for rendering



def email_message(request):
    pass