from django.db import models
from authentication_authorization.models import Registration

class Employee(models.Model):
	"""
		College Employee represents the database for employee record for initial setup
		and in future an admin can add and remove any user except himself to remove administrator 
		first administrator must be changed for the thedigitalcollege database
		
		Employee table relates it self with institution id


	"""	
	Gender = (
		('1',"Male"),
		('2',"Female"),
		('3',"Others")
	)
	Institution_ID = models.ForeignKey(Registration, on_delete = models.CASCADE)
	Employee_Name = models.CharField(max_length=100,null=True)
	Email = models.EmailField(max_length=100,unique=True,null=True)
	Password = models.CharField(max_length=25,default="123")
	Phone = models.CharField(max_length=15,unique=True,null=True,default="NON")
	Position = models.CharField(max_length=30,null=True)
	Salary = models.CharField(max_length=10,null=True,default="NON")
	Gender = models.CharField(max_length=1,default="o",choices=Gender)
	Tax_number = models.CharField(max_length=20,null=True, unique=True)
	About = models.CharField(max_length=200,null=True)
	Address = models.CharField(max_length=45,null=True)

	
	class Meta:
		db_table = 'Employee'
	

	def __str__(self):
		return self.Employee_Name




class Teacher(models.Model):	
	emoloyee= models.ForeignKey(Employee, on_delete=models.CASCADE)
	qualification = models.CharField(max_length=200,null=True)

	class Meta:
		db_table = 'Teacher'

	

class Student(models.Model):
	"""
		Responsible to manage students and their group

	"""
	name = models.CharField(max_length=60,null=True)
	student_id = models.AutoField(primary_key=True)
	address = models.CharField(max_length=80,null=True)
	number = models.CharField(max_length=15,null=True,blank=True)
	group = models.CharField(max_length=13,default='unassigned')



class Courses(models.Model):
	courses_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100,null=True)
	faculty = models.CharField(max_length=80,null=True)
	credit_hour = models.CharField(max_length=5,null=True)
	level = models.CharField(max_length=8,null=True)


class Classes(models.Model):
	"""
		Since many student can attend a single class 
		and one student can only be in one class 
		so, there is a many-to-one relation between class and student

		So one Course can have many classes but only one subject can be taught in
		a single class at a time so, 
		there resides a one-to-many relation between courses and the classes

		only one teacher is enough for a running class but
		there can be seperate teacher to a single class
		so there is many-to-one relation between classes and teacher

	"""
	classes_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=30,null=True)
	Course = models.ForeignKey(Courses,on_delete=models.CASCADE)
	Student = models.ForeignKey(Student,on_delete=models.CASCADE)
	Teacher  = models.ForeignKey(Teacher,on_delete=models.CASCADE)


class Assessment(models.Model):
	"""
			Since many students can work in a single assessment 
			and an assessment is assigned to each student 
			so there is many to one relation.
	"""
	# CHOICE_STATUS = (
	# 	('Done','Completed'),
	# 	()
	# )
	Assessment_name = models.CharField(max_length=100,null=True)
	Students = models.ForeignKey(Student, on_delete = models.CASCADE)

