from django.http import HttpResponse
from django.shortcuts import render, redirect
from first.models import Employee
from first.forms import EmployeeForm, LoginForm
from django.views import View
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
class EmployeeCreate(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'first/employee_form.html', {'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('.')


class EmployeeList(View):
    def get(self, request):
        emp = Employee.objects.all()
        return render(request, 'first/employee_list.html', {'emp': emp})


class LoginEmployee(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'first/employee_login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
        try:
            emp = Employee.objects.get(email=email, password=password)
        except ObjectDoesNotExist:
            resp="object does not exist"
            return HttpResponse(str(resp))
        return render(request, 'first/employee_login.html', {'emp': emp})
