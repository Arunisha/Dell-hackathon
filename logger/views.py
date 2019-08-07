from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .forms import LoginForm,CustomUserCreation


class LoginView(View):
	def get(self,request):
		form = LoginForm()
		return render(request,'logger/login.html',{'form':form})

	def post(self,request):
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
			if user is not None:
				login(request,user)
				return redirect('home')
		return redirect('login')
		

class SignupView(View):
	def get(self,request):
		form = CustomUserCreation()
		return render(request,'logger/signup.html',{'form':form})

	def post(self,request):
		form = CustomUserCreation(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'User created !')
			return redirect('login')
		messages.info(request,"Invalid information")
		return redirect('signup')


class LogoutView(View):
	def get(self,request):
		if request.user.is_authenticated:
			logout(request)
		return redirect('login')

