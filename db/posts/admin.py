from django.contrib import admin
from .models import Post, EmailMessage

admin.site.register(Post)
admin.site.register(EmailMessage)

