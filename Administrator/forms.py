from django import forms
from .models import Employee,Teacher
from django.forms import ModelForm

class Employee_Form(ModelForm):
	"""
		Manages all the employee
	# """
	required_css_class ='required'
	user_personal_mail = forms.CharField(
		max_length=30,
		widget=forms.TextInput(
			attrs={'placeholder': 'Personal Mail','autocomplete':'off'}
		),
		label = ""
	)
	class Meta:
		model = Employee
		fields =[
			'Institution_ID','Employee_Name','Email','Phone',
			'Position','Salary','Gender','Tax_number','About','Address'
		]
		widgets ={
			 'Employee_Name': forms.TextInput(attrs={'placeholder':'Employee Name'}),
			 'Email': forms.TextInput(attrs={'placeholder':'Email','autocomplete':'off'}),
			 'Position': forms.TextInput(attrs={'placeholder':'Position'}),
			 'Tax_number': forms.TextInput(attrs={'placeholder':'Tax number','autocomplete':'off'}),
			 'About': forms.TextInput(attrs={'placeholder':'About'}),
			 'Phone': forms.TextInput(attrs={'placeholder':'Phone'}),
			 'Salary': forms.TextInput(attrs={'placeholder':'NRS: Salary'}),
			 'Address':forms.TextInput(attrs={'placeholder':'Address'}),
		}

	

class Teacher_form(forms.Form):
	"""
		Responsible for all the teacher management
	"""
	class Meta:

		fields =[
			'emoloyee','qualification'
		]
		widgets ={
			'emoloyee': forms.TextInput(attrs={'placehoder':'Employee ID'}),
			'qualification': forms.Textarea(attrs={'placehoder': 'Qualification'})

		}