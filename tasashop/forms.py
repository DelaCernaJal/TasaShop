from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *



# class CheckoutFrms(forms.ModelForm):
# 	pass


# class registrationFrms(forms.ModelForm):
# 	username = forms.CharField(widget=forms.TextInput())
# 	password = forms.CharField(widget=forms.PasswordInput())
# 	email = forms.CharField(widget=forms.EmailInput())
# 	class meta:
# 		model = Customer
# 		fields = ['username','password','email', 'Fname', 'Lname', 'address']


class EntryForm(forms.ModelForm): 
	class Meta: 
		model = Entries 
		fields = ('artPrice','artName','artFile','artGcash','artBy')



class UserLoginForm(UserCreationForm): 
	class Meta: 
		model = User 
		fields = ['username', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super(UserLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class':'class-here', 'placeholder': 'Enter Username'})
		self.fields['email'].widget.attrs.update({'class':'class-here', 'placeholder': 'Enter Email'})
		self.fields['password1'].widget.attrs.update({'class':'class-here', 'placeholder': 'Enter Password'})
		self.fields['password2'].widget.attrs.update({'class':'class-here', 'placeholder': 'Confirm Password'})

















# class CustomerForm(forms.ModelForm):
# 	class Meta:
# 		model = Customer
# 		fields = ('address',)