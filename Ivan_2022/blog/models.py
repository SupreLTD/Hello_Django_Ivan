from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_updates = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField('Category', related_name='posts', blank=True)


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    posts = models.ForeignKey('Post', on_delete=models.CASCADE)
