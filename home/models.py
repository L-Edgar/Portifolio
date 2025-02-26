from django.db import models

# Create your models here.

class Project(models.Model):
    image=models.ImageField(upload_to='pics')
    status=models.BooleanField(default=True)
    link=models.CharField(max_length=100)
    type=models.CharField(max_length=10)

class Testimonial(models.Model):
    name=models.CharField(max_length=100)
    comment=models.TextField()
    occupation=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics',null=True,blank=True)

class Skill(models.Model):
    name=models.CharField(max_length=100)
    score=models.IntegerField()
    color=models.CharField(max_length=100)
    column=models.BooleanField(default=False)

