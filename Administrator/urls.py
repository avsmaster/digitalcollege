from django.urls import path
from Administrator.views import (
	Maxum_Administration,
	Maxum_Student,
	Maxum_Employee,
	Maxum_library
)

urlpatterns = [
	path('',Maxum_Administration.as_view()),
	path('/student/',Maxum_Student.as_view()),
	path('/employee/',Maxum_Employee.as_view()),
	path('/library/',Maxum_library.as_view()),
]