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
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Prepare the email content
            #subject = f"New Feedback from {name}"
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            recipient_list = [settings.EMAIL_HOST_USER]  # Your email
            
            # Send email
            send_mail(subject, full_message, email, recipient_list, fail_silently=False)
            
            return render(request, 'feedback_success.html', {'name': name})
    else:
        form = FeedbackForm()

    return render(request, 'feedback_form.html', {'form': form})