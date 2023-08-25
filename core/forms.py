# import the required libraries from django
from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# a class to set up the login of the user
class LoginForm(AuthenticationForm):
        username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-6 px-6 rounded-xl'
        }))
        password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class': 'w-full py-6 px-6 rounded-xl'
        }))

# similarly, a class to handle the signing up of the user
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    # for each field define the input in the form
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-6 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-6 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-6 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Retype password',
        'class': 'w-full py-6 px-6 rounded-xl'
    }))
    