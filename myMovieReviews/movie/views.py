from multiprocessing import context
from turtle import title
from django.shortcuts import redirect, render
from .models import Movie

# Create your views here.

def home(request):
    movie_lists = Movie.objects.all()
    
    context = {
        "movie_lists":movie_lists
    }
    return render(request, template_name="movie/home.html", context=context)

def create(request):
    if request.method == "POST":
        mytitle = request.POST["title"]
        myyear = request.POST["year"]
        mytype = request.POST["type"]
        mystar = request.POST["star"]
        mytime = request.POST["time"]
        myreview = request.POST["review"]
        mydirector = request.POST["director"]
        myactor = request.POST["actor"]
        
        Movie.objects.create(title=mytitle, year=myyear, type=mytype, 
star=mystar, time=mytime, review=myreview, director=mydirector, actor=myactor)
        return redirect('/')
    
    context = {}
    return render(request, template_name="movie/create.html", context=context)

def detail(request, id):
    movie = Movie.objects.get(id=id)
    
    context = {
        "movie": movie
    }
    
    return render(request, template_name="movie/detail.html", context=context)

def update(request, id):
    if request.method == "POST":
        mytitle = request.POST["title"]
        myyear = request.POST["year"]
        mytype = request.POST["type"]
        mystar = request.POST["star"]
        mytime = request.POST["time"]
        myreview = request.POST["review"]
        mydirector = request.POST["director"]
        myactor = request.POST["actor"]
        
        Movie.objects.filter(id=id).update(title=mytitle, year=myyear, type=mytype, 
star=mystar, time=mytime, review=myreview, director=mydirector, actor=myactor)
        return redirect(f"/review/{id}")
    
    elif request.method == "GET":
        movie = Movie.objects.get(id=id)
        context = {
            "movie": movie
        }
        
    return render(request, template_name='movie/update.html', context=context)

def delete(request, id):
    if request.method == "POST":
        Movie.objects.filter(id=id).delete()
        return redirect('/')