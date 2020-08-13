from django.urls import path
from first import views

urlpatterns=[
path('register/',views.user_register),
path('empregister/',views.emp_register),
path('login/',views.authenticate_user),
path('emplogin/',views.auth_employee),

]
