from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('like', 'liked')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post', 'user','like', 'liked')
        