from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length= 100, verbose_name="제목")
    year = models.IntegerField(verbose_name="개봉년도")
    type = models.CharField(max_length= 100, verbose_name="장르")
    star = models.CharField(max_length=5, verbose_name="별점")
    time = models.IntegerField(verbose_name="러닝타임")
    review = models.TextField(verbose_name="리뷰")
    director = models.CharField(max_length=50, verbose_name="감독")    
    actor = models.CharField(max_length=50, verbose_name="배우")

