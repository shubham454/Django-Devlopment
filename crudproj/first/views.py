from django.shortcuts import render, redirect
from first.models import Employee

# Create your views here.
def all_emp(request):
    data = Employee.objects.all()
    return render(request,'first/home.html',{'data':data})

def add_emp(request):
    if request.method == 'POST':
        name = request.POST.get('ename')
        salary = request.POST.get('esalary')
        company = request.POST.get('ecompany')
        e = Employee(ename = name, esalary = salary, ecompany = company)
        e.save()
        return redirect('/first/all/')
    return render(request, 'first/add.html')

def delete_emp(request,id):
    obj = Employee.objects.get(pk = id)
    obj.delete()
    return redirect('/first/all/')

def update_emp(request,id):
    obj = Employee.objects.get(pk = id)
    if request.method == "POST":
        obj.ename = request.POST.get('ename')
        obj.esalary = request.POST.get('esalary')
        obj.ecompany = request.POST.get('ecompany')
        obj.save()
        return redirect('/first/all/')
    return render(request, 'first/update.html',{'obj':obj})
