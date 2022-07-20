from django.shortcuts import redirect, render
from .models import Post

#home
def home(request):
    posts = Post.objects.all()

    context = {
        "posts":posts
    }
    return render(request, template_name = "posts/home.html", context=context)

#Create
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        image = request.FILES["image"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        devtool = request.POST["devtool"]
    
        Post.objects.create(title=title, image=image, content=content, interest=interest, devtool=devtool)

        return redirect('/')

    context = {}
    return render(request, template_name='posts/create.html', context=context)

def detail(request, id):
    post = Post.objects.get(id=id)
    
    context = {
        "post": post,
    }
    
    return render(request, template_name='posts/detail.html', context=context)

# Update
def update(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        image = request.FILES["image"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        devtool = request.POST["devtool"]
        
        Post.objects.filter(id=id).update(title = title, image=image, content=content, interest=interest, devtool=devtool)
        return redirect(f"/post/{id}")
        
    elif request.method == "GET":
        post = Post.objects.get(id=id)
        context = {
            "post": post
        }
    
    return render(request, template_name='posts/update.html', context=context)

# Delete
def delete(request, id):
    if request.method == "POST":
        Post.objects.filter(id=id).delete()
        return redirect('/')