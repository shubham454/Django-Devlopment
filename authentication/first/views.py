from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from first.forms import LoginForm,EmployeeForm
from django.contrib import auth,messages
from django.core.exceptions import ObjectDoesNotExist
from first.models import Employee
# Create your views here.
def user_register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request,'first/register.html',{'form':form})
    return render(request,'first/register.html',{'form':form})


def emp_register(request):
    form = EmployeeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request,'first/empregister.html',{'form':form})
    return render(request,'first/empregister.html',{'form':form})

def authenticate_user(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            print("in try")
            user = auth.authenticate(username=username,password=password)
            print(user)
            if user is not None:
                auth.login(request,user)
                return render(request,'first/success.html')
            else:
                messages.error(request,'enter correct username and password')
        except User.DoesNotExist:
            print('user does not exist')
    return render(request,'first/loginform.html', {'form':form})

def auth_employee(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            print("in try")
            emp = Employee.objects.get(ename=username,epass=password)
            print(user)
        except Employee.DoesNotExist:
            emp=None

        if emp is not None:
            Employee.login(request,user)
            return render(request,'first/success.html')
        else:
            messages.error(request,'enter correct username and password')
    return render(request,'first/loginform.html', {'form':form})
