from django.db import models

# Create your models here.
class modelBlog(models.Model):
    title=models.CharField(max_length=30)
    summary=models.TextField(max_length=5000)
