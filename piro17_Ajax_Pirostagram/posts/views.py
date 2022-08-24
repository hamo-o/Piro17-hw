from django.shortcuts import render, redirect, get_object_or_404
from posts.forms import CommentForm, PostForm
from .models import Post, Comment

# Create your views here.

def home(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:home')
        else:
            context = {
                'posts': posts,
                'form': form,
            }
            return render(request, "posts/home.html", context=context)
    elif request.method == "GET":
        form = PostForm()
        context = {
            'posts': posts,
            'form': form,
        }
        return render(request, "posts/home.html", context=context)

# def create(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:home')
#         else:
#             context = {
#                 'form': form,
#             }
#             return render(request, "posts/home.html", context=context)
#     elif request.method == "GET":
#         form = PostForm()
#         context = {
#             'form': form,
#         }
#         return render(request, "posts/home.html", context=context)

# def detail(request, id):
#     post = Post.objects.get(id=id)
#     comments = Comment.objects.filter(post=id)
#     context = {
#         "post": post,
#         "comments": comments,
#     }
#     return render(request, template_name='posts/detail.html', context=context)

# def create_comment(request, id):
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment=form.save(commit=False)
#             comment.post=post
#             comment.save()
#             return redirect('detail', id)
#         else:
#             form=CommentForm()

def delete(request, id):
    if request.method == "POST":
        Post.objects.filter(id=id).delete()
        return redirect('/')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request):
    request = json.loads(request.body) 
    post_id = request['id'] 
    post = Post.objects.get(id = post_id)

    if post.liked == True:
        post.liked = False
        status = post.liked
        post.like = '<i class="fa-solid fa-heart"></i>'
        message = "좋아요 취소"
    else:
        post.liked = True
        status = post.liked
        post.like ='<i class="fa-solid fa-heart" style="color:red"></i>'
        message = "좋아요"
    post.save()

    return JsonResponse({'id': post_id, 'message': message, 'status':status})

@csrf_exempt
def delete_ajax(request):
    request = json.loads(request.body) 
    post_id = request['id'] 
    Post.objects.filter(id = post_id).delete()

    return JsonResponse({'id': post_id })