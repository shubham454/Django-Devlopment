from django import forms
from first.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

class LoginForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()
