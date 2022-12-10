from django.core import validators
from django import forms
from .models import User,Post

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ["user_name","user_email","user_password","user_phone"]
        widgets = {
   'user_name': forms.TextInput(attrs={'class':'form-control'}),
   'user_email': forms.EmailInput(attrs={'class':'form-control'}),
   'user_phone': forms.TextInput(attrs={'class':'form-control'}),
   'user_password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
  }


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["user_email","user_password"]
        widgets = {
   'user_email': forms.EmailInput(attrs={'class':'form-control'}),
   'user_password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
  }


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","body"]
        widgets = {
   'title': forms.TextInput(attrs={'class':'form-control'}),
   'body': forms.Textarea(attrs={'class':'form-control'})
  }
