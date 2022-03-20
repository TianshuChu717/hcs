from django import forms
from django.contrib.auth.models import User
from app.models import UserProfile


class UserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'password', )