from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Entries



# class CheckoutFrms(forms.ModelForm):
# 	pass


class EntryForm(forms.ModelForm): 
	class Meta: 
		model = Entries 
		fields = ['artprice','artname','artgcash','artfile',]

	def __init__(self, *args, **kwargs):
		super(EntryForm, self).__init__(*args, **kwargs)
		self.fields['artprice'].widget.attrs.update({'placeholder': 'Enter price'})
		self.fields['artname'].widget.attrs.update({'placeholder': 'Enter art name'})
		self.fields['artgcash'].widget.attrs.update({'placeholder': 'Gcash Account'})
		self.fields['artfile'].widget.attrs.update({'placeholder': 'Upload art '})

class UserLoginForm(UserCreationForm): 
	class Meta: 
		model = User 
		fields = ['username', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super(UserLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'placeholder': 'Enter Username'})
		self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
		self.fields['password1'].widget.attrs.update({'placeholder': 'Enter Password'})
		self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})


# class cosdesign(forms.ModelForm): 
# 	class Meta: 
# 		model = CartItem 
# 		fields = ['cdesign', 'quan']


# class CustomerForm(forms.ModelForm):
# 	class Meta:
# 		model = Customer
# 		fields = ('address',)