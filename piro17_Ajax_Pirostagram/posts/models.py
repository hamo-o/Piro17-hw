from statistics import mode
from django.db import models

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=20)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")
    content = models.CharField(max_length=200)
    like = models.TextField(default= '<i class="far fa-heart"></i> ')
    liked = models.BooleanField(default=False)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cmt_user")
    content = models.CharField(max_length=200)
    like = models.TextField(default= '<i class="far fa-heart"></i> ')
    liked = models.BooleanField(default=False)