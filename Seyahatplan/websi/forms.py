from django import forms
from .models import ContactMessage

class Contactform(forms.ModelForm):
    class Meta:
        model=ContactMessage
        fields=['name','phone_number','email','message']