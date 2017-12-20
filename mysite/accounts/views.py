from django.shortcuts import render,redirect
from django.contrib.auth import(
	login,
	logout,
	get_user_model,
	authenticate,
	) 
from .forms import UserLoginForm,UserRegisterForm

def login_view(request):
	title = "Drizzlelore"
	subtitle = "Login"
	button_value = "LOGIN"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request,user)
		#print(request.user.is_authenticated())
		#print(user.get_username)
		return redirect("/")
	return render(request,"accounts/form.html",{"form":form, "title":title, "subtitle":subtitle, "button_value":button_value,})

def register_view(request):
	title = "Drizzlelore"
	subtitle = "Register"
	button_value = "REGISTER"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		#newuser = authenticate(username=user.username,password=password)
		login(request,user)	
		return redirect("/")
	context = {
		"form":form,
		"title":title,
		"subtitle":subtitle,
		"button_value":button_value,
	}
	return render(request,"accounts/form.html",context)

def logout_view(request):
	logout(request)
	button_value = ""
	return render(request,"accounts/form.html",{"button_value":button_value,})
