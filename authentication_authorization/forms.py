from django import forms
from django.forms import ModelForm
from .models import Registration

class Message_form(forms.Form):
	"""
		Responsible for form creation, validation and verification
		for suggestion contact list and more
	"""
	name =forms.CharField(max_length=100,label='Name')
	email=forms.EmailField(label='email address')
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea) #for texts
	cc_myself = forms.BooleanField(required=False)

class User_Registration(ModelForm):
	"""
		Responsible for user registration
	"""
	required_css_class = 'required'
	conform_password = forms.CharField(
		max_length=30,widget=forms.PasswordInput(
			attrs={'placeholder':'confirm-password','autocomplete':'off'}
		)
	) # to verify passoword

	class Meta:
		model = Registration
		fields = [
			'Institution_Name','Admin_Name','Admin_Email','Institution_type','Admin_Password',
			'Number_of_student','Number_of_employee','Institution_registration_number',
			'Brief_description','Admin_Phone'
		]
		widgets ={
			'Institution_Name': forms.TextInput(attrs={'placeholder':'Institution Name'}),
			'Admin_Name': forms.TextInput(attrs={'placeholder':'Admin Name'}),
			'Admin_Password':forms.PasswordInput(
				attrs={
					'placeholder':'password',
					'autocomplete':'off'
				}
			),
			'Institution_registration_number': forms.TextInput(attrs={
				'placeholder': 'Institution Registration Number'
			}),
			'Admin_Phone': forms.TextInput(attrs={'placeholder':'Phone'}),
			'Admin_Email': forms.TextInput(attrs={
				'placeholder':'Admin Email',
				'autocomplete':'off'
			}),
			'Brief_description': forms.Textarea(attrs={
				'placeholder':'About'
			})
		}
		

class User_Login(forms.Form):
	"""
		Responsible for all the user login credentials
	"""
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'mail'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'placeholder':'password'}))