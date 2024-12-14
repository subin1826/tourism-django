from django import forms
from.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserReistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']

class Userloginform(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']

class Packageform(forms.ModelForm):
    class Meta:
      model=Package
      fields=['name','description','main_viewpoint','price','duration','media_gallery']

class Vendorform(forms.ModelForm):
    class Meta:
      model=Vendor
      fields='__all__'
      
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=20, label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
      
      
