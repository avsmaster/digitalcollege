from django.urls import path
from . import views
from authentication_authorization.views import Signup,Index

#paths
urlpatterns =[
	path('',Index.as_view()),
	path('login',views.login,name='login'),
	path('signup',Signup.as_view()),
]