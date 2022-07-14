from multiprocessing import context
from django.shortcuts import render
from .models import Movie

# Create your views here.

def home(request):
    movie_lists = Movie.objects.all()
    
    context = {
        "movie_lists":movie_lists
    }
    return render(request, template_name="movie/home.html", context=context)

def create(request):
    pass
    