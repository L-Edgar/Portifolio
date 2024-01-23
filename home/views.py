from django.shortcuts import render
from .models import Project
# Create your views here.

def index(request):
    return render(request,'index.html')

def projects(request):
    projects=Project.objects.all()

    return render(request,'projects.html',{"projects":projects})

def contact(request):
    return render(request,'contact.html')