from django.contrib import admin

from .models import (
	Employee,Teacher,Classes,Student,Courses,
	Assessment
)
# Register your models here.

admin.site.register(Employee)
admin.site.register(Teacher)

admin.site.register(Classes)
admin.site.register(Student)

admin.site.register(Courses)
admin.site.register(Assessment)
