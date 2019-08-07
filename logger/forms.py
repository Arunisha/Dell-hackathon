from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreation(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username','email','first_name','last_name','age')


class CustomUserChange(UserChangeForm):
	class Meta(UserChangeForm):
		model = CustomUser
		fields = ('username','email','first_name','last_name','age','num_bought','num_added','num_discarded')




class LoginForm(forms.Form):
	username = forms.CharField(max_length=150)
	password = forms.CharField(max_length=50, widget=forms.PasswordInput)


