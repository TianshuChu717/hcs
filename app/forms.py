from django import forms
from django.contrib.auth.models import User
from app.models import UserProfile
   
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'password','email','money')
