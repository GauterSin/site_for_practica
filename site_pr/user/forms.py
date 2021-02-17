from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput



class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class SingInFrom(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))