from django.db import models

class Registration(models.Model):
	""" Registratiion model in thedigitalcollege is responsible for all the registration 
      of different colleges and schools
      
       1. Institution_ID : represents the unique institution id determined by thedigitalcollege 
       2. Institution_Name : represents the unique name as per registration under Nepals constitution act 
       3. Admin_ID : represents the unique administrator id 
       4. Admin_Name : represents the admin name
       5. Admin_Email : represents the admin emial
       6. Institution_type : school or college or university or tution centre 
       7. Number_of_student : total initial capacity can be increased or decreased in future
       8. Number_of_employee : total number of current employee
       9. Institution_registration_number : legal registration 
       10 Brief_description : brief description about the institution
       11. Date_of_registration: details about date and time of registration
              
    """  
      #help texts

	Institution_TYPE_CHOICES = (
		('C','college'),
		('S','school'),
		('o','others'),
	)
	NUMBER_CHOICES = (
		(1,'0-100'),
		(2,'100-1000'),
		(3,'1000+'),
	)
	Institution_Name= models.CharField(max_length=180,unique=True, help_text="")
	Institution_ID = models.AutoField(primary_key=True)
	Admin_Name =models.CharField(max_length=60,null=True)
	Admin_Password = models.CharField(max_length=30,null=True)
	Admin_Email = models.EmailField(max_length=100,unique=True,null=True)
	Admin_Phone = models.CharField(max_length=30,unique=True,null=True)
	Institution_type = models.CharField(max_length=2,default='o',choices=Institution_TYPE_CHOICES)
	Number_of_student = models.IntegerField(default=1,choices=NUMBER_CHOICES)
	Number_of_employee =models.IntegerField(default=1,choices=NUMBER_CHOICES)
	Institution_registration_number =models.CharField(max_length=180,unique=True,null=True)
	Brief_description = models.TextField('About Institution',blank=True)

	def __str__(self):
		return self.Institution_Name