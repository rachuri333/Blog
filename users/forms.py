from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile

class reistrationform(UserCreationForm):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']


class userupdateform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']

class profileupdateform(forms.ModelForm):
    class Meta:
        model=profile
        fields=['image']