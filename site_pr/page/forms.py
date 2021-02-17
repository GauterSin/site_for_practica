from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea
from .models import Post, Comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'content']
        widgets = {
            "name": TextInput(attrs={
                'class':'form-label',
                'type':"text"
            }),
            'content': Textarea(attrs={
                'cols': 30, 
                'rows': 10
            })

        }
    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={
                'cols': 30, 
                'rows': 10
            }),
        }
