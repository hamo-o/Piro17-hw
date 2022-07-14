from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('review/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.update, name="update"),
]