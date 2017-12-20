from django import forms
from django.contrib.auth import(
	login,
	logout,
	get_user_model,
	authenticate,
	) 

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if username and password:
			user = authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError("This user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")
			if not user.is_active:
				raise forms.ValidationError("This user not longer active")
		return super(UserLoginForm,self).clean()

class UserRegisterForm(forms.ModelForm):

	email = forms.EmailField(label = 'Email Address')
	email2 = forms.EmailField(label = 'Confirm Email')
	password = forms.CharField(widget = forms.PasswordInput)
	
	class Meta:
		model = get_user_model()
		fields = [
			'username',
			'email',
			'email2',
			'password',
		]
		help_texts = {
			'username' : None,
			'email' : None,
			'email2' : None,
			'password' : None,
		}

	# def clean(self):
	# 	email = self.cleaned_data.get('email')
	# 	email2 = self.cleaned_data.get('email2')
	# 	if email != email2:
	# 		raise forms.ValidationError("Emails must match")
	# 	email_qs = get_user_model().objects.filter(email=email)
	# 	if email_qs.exists():
	# 		raise forms.ValidationError("This email has already been registered")
	# 	return super(UserRegisterForm,self).clean()


	def clean_email2(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError("Emails must match")
		email_qs = get_user_model().objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email has already been registered")
		return email