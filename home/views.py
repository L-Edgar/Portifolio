from django.shortcuts import render
from .models import Project, Testimonial, Skill

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    projects=Project.objects.all()
    testimonials=Testimonial.objects.all()
    skills=Skill.objects.all()
    return render(request,'index.html',{'projects':projects, 'testimonials':testimonials,'skills':skills})

