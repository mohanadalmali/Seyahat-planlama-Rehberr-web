from django import forms
from .models import Comment

class Commentform(forms.ModelForm):
    class Meta:
        model=Comment
        template_name='add_comment.html'
        fields=('name','body')
        
        widgets={
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
        }
        