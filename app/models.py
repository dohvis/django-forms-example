from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return '{} {}'.format(self.__class__.__name__, self.title)


class Tag(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return '{} {}'.format(self.__class__.__name__, self.title)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    category = models.ForeignKey(Category, related_name='posts', null=True)
    tag = models.ManyToManyField(Tag, related_name='posts')
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return '{} {}'.format(self.__class__.__name__, self.title)


class Comment(models.Model):
    parent_post = models.ForeignKey(Post, related_name='comments')
    author = models.ForeignKey(User, related_name='comments')
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.__class__.__name__, self.title)
