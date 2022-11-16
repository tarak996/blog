from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import modelBlog
class singup(UserCreationForm):
    password2=forms.CharField(label='conform password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

class formBlog(forms.ModelForm):
    class Meta:
        model=modelBlog
        fields='__all__'