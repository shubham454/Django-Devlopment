from django import forms
from first.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
