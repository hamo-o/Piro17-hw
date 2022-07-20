from django.shortcuts import redirect, render
from .models import Post, Tool

#home
def home(request):
    posts = Post.objects.all()
    
    sort = request.GET.get('sort', 'None')
    if sort == "name":
       posts = posts.order_by("title")
    elif sort == "createAt":
       posts = posts.order_by("created_at")
    elif sort == "updateAt":
       posts = posts.order_by("-updated_at")

    context = {
        "posts":posts
    }
    return render(request, template_name = "posts/home.html", context=context)

#Create
def create(request):
    tools = Tool.objects.all()
    if request.method == "POST":
        title = request.POST["title"]
        image = request.FILES["image"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        devtool = request.POST["devtool"]
        for tool in tools:
            if tool.name == devtool:
                devtool = tool
    
        Post.objects.create(title=title, image=image, content=content, interest=interest, devtool=devtool)

        return redirect('/')

    TOOL_LIST = []
    for tool in tools:
        TOOL_LIST.append(tool.name)
    
    context = {'tool_list':TOOL_LIST}
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
    
# home2
def dev(request):
    tools = Tool.objects.all()
    
    context = {
        "tools":tools
    }
    return render(request, template_name = "posts/dev.html", context=context)

# Create2
def dev_create(request):
    if request.method == "POST":
        name = request.POST["name"]
        type = request.POST["type"]
        content = request.POST["content"]
        
        Tool.objects.create(name=name, type=type, content=content)
        
        return redirect('/dev')

    context = {}
    return render(request, template_name='posts/dev_create.html', context=context)

def dev_detail(request, id):
    tool = Tool.objects.get(id=id)
    
    all_post = tool.post_tool.all()
    
    context = {
        "tool":tool,
        "all_post":all_post,
    }
    
    return render(request, template_name='posts/dev_detail.html', context=context)

# Update2
def dev_update(request, id):
    if request.method == "POST":
        name = request.POST["name"]
        type = request.POST["type"]
        content = request.POST["content"]
        
        Tool.objects.filter(id=id).update(name = name, type=type, content=content)
        return redirect(f"/tool/{id}")
        
    elif request.method == "GET":
        tool = Tool.objects.get(id=id)
        context = {
            "tool": tool
        }
    
    return render(request, template_name='posts/dev_update.html', context=context)

# Delete
def dev_delete(request, id):
    if request.method == "POST":
        Tool.objects.filter(id=id).delete()
        return redirect('/dev')
