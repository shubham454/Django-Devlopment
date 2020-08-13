from django.shortcuts import render
from test1.models import Employee

# Create your views here.
def all_employee(request):
    data = Employee.objects.all()
    return render(request,'test1/home.html',{'data':data})

def filter1(request):
    data = Employee.objects.filter(name = 'shubham')
    return render(request,'test1/home.html',{'data':data})

def filter2(request):
    data = Employee.objects.filter(salary__lt = 20000)
    return render(request,'test1/home.html',{'data':data})

def filter3(request):
    data = Employee.objects.filter(salary__gt = 15000)
    return render(request,'test1/home.html',{'data':data})

def filter4(request):
    data = Employee.objects.filter(company__iexact = 'miCroSoft')
    return render(request,'test1/home.html',{'data':data})

def filter5(request):
    data = Employee.objects.filter(company__contains = 'm')
    return render(request,'test1/home.html',{'data':data})
