from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import User

# class signup_form(forms.Form):
# 	# newUsername = forms.CharField(max_length=100)
# 	# newPassword = forms.CharField(max_length=100)
# 	# newFirstName = forms.CharField(max_length=25)
# 	# newLastName = forms.CharField(max_length=25)

# 	class Meta:
# 		model = User
# 		fields = ['username','password','newFirstName','newLastName']

# 	# def __str__(self):
# 	# 	return self.newUsername


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = (
				'first_name',
				'last_name',
				'username',
				'password1',
				'password2',
				'email'
		)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

