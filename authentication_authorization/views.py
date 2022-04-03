from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . forms import Message_form,User_Registration,User_Login
from django.core.mail import send_mail, get_connection #for messages
from django.views import View
from Administrator.models import Employee
from .models import Registration


#All the thedigitalcollege views
class Index(View):
	"""
		Handles the Index page
	"""
	#form that handles all the messeges sent 
	def __init__(self):
		self.submitted=False
		self.form_class= Message_form

	def post(self,request):
		#creates the from and populate it with the data from the requst
		form = self.form_class(request.POST)
		#check whether the entered data is valid
		if form.is_valid():
			#process the data from the form
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			cc_myself = form.cleaned_data['cc_myself']
			data=form.cleaned_data
			recipients = ['info.support@thedigitalcollege.org']

			#to message backend
			con= get_connection('django.core.mail.backends.console.EmailBackend')
			
			#in future maneges emailserver
			send_mail(subject,message,data.get(
				'email','noreply@thedigitalcollege.org'
			),recipients,connection=con)
			
			#redirect to the new url
			self.submitted=True
			return HttpResponseRedirect('')
	#for any other request
	def get(self, request):
		login_form = User_Login()
		form = Message_form()
		CONTEXT = {
			'form':form,
			'login_form':login_form,
			'submitted':self.submitted
		}
		return render(request,'index.html',CONTEXT)


class Signup(View):
	"""
		Responsible for institution registration and admin creation

	"""	
	form_class = User_Registration
	template_name = 'signup.html'
	login_form = User_Login
	#for get request
	def get(self,request):
		form = self.form_class()
		login = self.login_form()
		return render(request, self.template_name,{'form':form,'login_form':login})

	#for post request
	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			password=form.cleaned_data['Admin_Password']
			conform_password = form.cleaned_data['conform_password']
			if self.validate_password(password,conform_password):
				form.save()
				# Creating Account for admin in recent suscribed institution
				institution = form.cleaned_data['Institution_Name']
				# Saving in the employee table 
				employee = Employee()
				employee.Institution_ID = Registration.objects.get(Institution_Name=institution)
				employee.Employee_Name = form.cleaned_data['Admin_Name']
				employee.Email = form.cleaned_data['Admin_Email']
				employee.Password = form.cleaned_data['Admin_Password']
				employee.About =form.cleaned_data['Brief_description']
				employee.Position = "Admin"
				employee.Phone = form.cleaned_data['Admin_Phone']
				employee.save() #save data

				# Sending welcome mail done Done Done
				con = get_connection('django.core.mail.backends.console.EmailBackend')
				# send_mail(subject, message,from,to,connection)
				send_mail(
					"Institution Registration successfull",
					"Hello {0}, \n"+
					"welcoome to thedigitalcollege Family.".format(form.cleaned_data['Admin_Name']),
					form.cleaned_data.get("email",'info.support@thedigitalcollege.org'),
					(form.cleaned_data['Admin_Email'],),
					connection=con					
				)
				# creating a session 
				request.session['institute_data_login']=institution
				request.session['Admin'] = form.cleaned_data['Admin_Name']
				# Create and Manage session
				return HttpResponseRedirect('dashboard')
			else:
				return render(request, self.template_name,{'form':form,'p_er':'error'})

		return render(request, self.template_name,{'form':form})

	def validate_password(self,password,re_entered_password):
		# right now just a passwod matching : password hashinf and more are 
		#done by this
		if password == re_entered_password: return True
		else: return False


def login(request):
	return HttpResponseRedirect('dashboard')
	

