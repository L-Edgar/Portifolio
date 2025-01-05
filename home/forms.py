from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Your Name'
        }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Your Email'
        }))
    subject=forms.CharField(max_length=100,required=False,  widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'subject',
            'placeholder': 'Subject'
        }))
    message = forms.CharField(widget=forms.Textarea, required=True, widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'message',
            'placeholder': 'Message',
            'style': 'height: 100px'
        }))