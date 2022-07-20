from django.contrib import admin

# Register your models here.

from .models import Post, Tool

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Tool)
class PostAdmin(admin.ModelAdmin):
    pass