from django import forms
from django.forms import ModelForm
from .models import List
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ListForm(forms.ModelForm):

	class Meta:
		model = List
		fields = ['firstname','lastname','email','phone_number']

class RegistrationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username','email','password1','password2']