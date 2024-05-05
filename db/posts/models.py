from django.db import models

class Post(models.Model):
    """inherited by Django model to describe DB model"""
    post = models.CharField(max_length=75)


    def __str__(self):
        return self.post