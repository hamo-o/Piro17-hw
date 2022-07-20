from django.db import models

# Create your models here.


class Post(models.Model):
    DEVTOOL_CHOICES = (
        ('RA', 'React'),
        ('DJ', 'Django'),
        ('NJ', 'Nodejs'),
    )
    title = models.CharField(verbose_name ="제목", max_length=50)
    image = models.ImageField(verbose_name ="이미지", upload_to='posts/%Y%m%d', height_field=None, width_field=None, max_length=None)
    content = models.TextField(verbose_name ="내용")
    interest = models.CharField(verbose_name ="관심도", max_length=50)
    devtool = models.CharField(verbose_name ="개발툴", max_length=50, choices=DEVTOOL_CHOICES)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)