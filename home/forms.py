from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
   class Meta:
        model = Feedback
        fields = ['name', 'email', 'message','subject']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'}),
        }
       