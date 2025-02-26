from django.shortcuts import render
from .models import Project, Testimonial, Skill
from .forms import FeedbackForm


# Create your views here.

def home(request):
    projects=Project.objects.all()
    testimonials=Testimonial.objects.all()
    skills=Skill.objects.all()
    return render(request,'index.html',{'projects':projects, 'testimonials':testimonials,'skills':skills})

def feedback_view(request):
    form=FeedbackForm()
    return render(request, 'index.html', {'form': form})