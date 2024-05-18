from django.db import models

class Post(models.Model):
    """inherited by Django model to describe DB model"""
    post = models.CharField(max_length=75)

    def __str__(self):
        return self.post

class EmailMessage(models.Model):
    name = models.CharField(max_length=10)
    email_message = models.EmailField(max_length=20)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name