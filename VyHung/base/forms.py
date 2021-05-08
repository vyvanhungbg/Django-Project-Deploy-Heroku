from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Profile


class CustomUserCreationForm(UserCreationForm):
    
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
	def clean_email(self):
		email = self.cleaned_data.get('email')
		
		if email =='':
			raise forms.ValidationError("Email cannot be empty or null !")
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("email was already registered !")
		return email

		
		


class PostForm(ModelForm):

	class Meta:
		model = Post
		fields = '__all__'

		widgets = {
			'tags':forms.CheckboxSelectMultiple(),
		}

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']
	

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['user']

