from django import forms
from .models import Post

class post_model_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        labels = {
            'title': '',
            'body': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'body': forms.Textarea(attrs={'class': 'form-control mb-3'})
        }