from django.shortcuts import render
from .models import Project, Testimonial, Skill
from .forms import FeedbackForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def home(request):
    projects=Project.objects.all()
    testimonials=Testimonial.objects.all()
    skills=Skill.objects.all()
    return render(request,'index.html',{'projects':projects, 'testimonials':testimonials,'skills':skills})

def feedback_view(request):
    form=FeedbackForm()
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            
             # Email content
            subject = f"New Feedback from {name}"
            full_message=f"Message from {name} ({email}):\n\n{message}"
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['lelishaedgar10@gmail.com'],  # <-- Replace with your own email
                fail_silently=False,
            )
            
            #return render(request, 'index.html', {'form': FeedbackForm(), 'success': True})
    return render(request, 'index.html', {'form': form})