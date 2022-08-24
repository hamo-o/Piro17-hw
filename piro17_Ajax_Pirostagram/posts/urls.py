from django.urls import path 

from . import views

app_name = "posts"

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>', views.delete, name="delete"),
    path('like_ajax/',views.like_ajax, name='like_ajax'),
    path('delete_ajax/',views.delete_ajax, name='delete_ajax'),
    path('create_ajax/',views.create_ajax, name='create_ajax'),
]