from django.shortcuts import render, redirect, get_object_or_404
from posts.forms import CommentForm, PostForm
from .models import Post, Comment

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/home.html', context=context)

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:home')
        else:
            context = {
                'form': form,
            }
            return render(request, "posts/create.html", context=context)
    elif request.method == "GET":
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request, "posts/create.html", context=context)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    
    context = {
        "post": post,
    }
    
    return render(request, template_name='posts/detail.html', context=context)

def delete(request, id):
    if request.method == "POST":
        Post.objects.filter(id=id).delete()
        return redirect('/')

def comment_create(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        cmt_form = CommentForm(request.POST)
        if cmt_form.is_valid():
            comment = cmt_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
        return redirect('posts:detail', post.pk)
    return redirect('/')

def comment_delete(request, post_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('posts:detail', post_pk)
    

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request):
    request = json.loads(request.body) 
    post_id = request['id'] 

    post = Post.objects.get(id = post_id)

    if post.liked == True: #좋아요가 눌러져있으면
        post.liked = False
        status = post.liked
        post.like = '<i class="fa-solid fa-heart"></i>'
        message = "좋아요 취소"
    else: #좋아요가 안눌러져있으면
        post.liked = True
        status = post.liked
        post.like ='<i class="fa-solid fa-heart" style="color:red"></i>'
        message = "좋아요"
    post.save()

    return JsonResponse({'id': post_id, 'message': message, 'status':status})