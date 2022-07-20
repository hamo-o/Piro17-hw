from django.contrib import admin
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('post/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('dev', views.dev, name="dev"),
    path('dev_create', views.dev_create, name="dev_create"),
    path('tool/<int:id>', views.dev_detail, name="dev_detail"),
    path('dev_update/<int:id>', views.dev_update, name="dev_update"),
    path('dev_delete/<int:id>', views.dev_delete, name="dev_delete"),
]
