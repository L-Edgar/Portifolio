from django.db import models

# Create your models here.

class Project(models.Model):
    image=models.ImageField(upload_to='pics',null=True,blank=True)
    description=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    link=models.CharField(max_length=200)