from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from .models import Employee
from .forms import Employee_Form
# EMAIL
from django.core.mail import send_mail, get_connection

class Maxum_Administration(View):

	def get(self,request):
		# Session Management
		# Get users
		# student Student.objects.get(Institution_ID=request.session['Institution'])
		return render(request,'dashboard.html')
		
	

class Maxum_Student(View):
	"""Responsible for Student Management"""
	def get(self, request):
		return render(request,'classes_dashboard.html')

class Maxum_Employee(View):
	"""
		Employee 
	"""
	
	form_class = Employee_Form
	template_name = 'employee_dashboard.html'

	def get(self, request):
		form = self.form_class()
		
		employee=[]
		for i,v in enumerate(Employee.objects.all()):
			employee.append((i,v))
		return render(request,self.template_name,{'form':form,'employee':dict(employee)})

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save() #saves the form
			name = form.cleaned_data['Employee_Name']
			email = form.cleaned_data['Email']
			tax_number = form.cleaned_data['Tax_number']
			about = form.cleaned_data['About']
			recipient = form.cleaned_data['user_personal_mail']


			# sending mail as employee added  add mail server on
			con = get_connection('django.core.mail.backends.console.EmailBackend')

			#send mail
			send_mail(
				"Letter of Acceptance",
				"welcome to our family",
				form.cleaned_data.get(
					'email','norply@thedigitalcollege.com'
				),(recipient,),connection=con
			)
			
		return HttpResponseRedirect('/dashboard/employee')
		
class Maxum_library(View):
	# Responsible For Library Management
	def get(self, request):
		return render(request,'Dashboard_library.html')
