from django import forms
from first.models import Employee
from django.core import validators

class EmployeeForm(forms.ModelForm):
    esalary = forms.IntegerField(validators=[validators.MinValueValidator(8000)])
    class Meta:
        model=Employee
        fields=['ename','eaddress','esalary','experience','gender']

class LoginForm(forms.Form):
    ename = forms.CharField()
    eaddress = forms.CharField()
