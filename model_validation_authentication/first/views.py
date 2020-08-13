from django.shortcuts import render,redirect
from first.models import Employee
from first.forms import EmployeeForm,LoginForm
from django.views.generic import View
from django.contrib import auth, messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class EmployeeAdd(View):
    def get(self,request):
        form = EmployeeForm()
        return render(request,'first/add.html',{'form':form})
    def post(self,request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list')
        return render(request,'first/add.html',{'form':form})

class EmployeeRead(View):
    def get(self,request,id=None,*args,**kwargs):
        emp = Employee.objects.all()
        # emp = Employee.objects.filter(esalary__gt=10000)
        # emp = Employee.objects.filter(esalary__lt=10000)
        # emp = Employee.objects.get(id = id)
        return render(request,'first/list.html',{'emp':emp})

class EmloyeeDelete(View):
    def get(self,request,id):
        emp = Employee.objects.get(id=id)
        emp.delete()
        return redirect('/list/')

class EmployeeUpdate(View):
    def get(self,request,id):
        emp = Employee.objects.get(id=id)
        form = EmployeeForm(instance=emp)
        return render(request, 'first/update.html',{'form':form,'emp':emp})
    def post(self,request,id):
        emp = Employee.objects.get(id=id)
        form = EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/list/')
        return render(request, 'first/update.html',{'form':form})

class LoginEmployee(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'first/login.html',{'form':form})
    def post(self,request):
        ename = request.POST.get('ename')
        eaddress = request.POST.get('eaddress')
        try:
            emp = Employee.objects.get(ename=ename,eaddress=eaddress)
            if emp is not None:
                Employee.login(request,emp)
                # session create
                request.session['ename'] = emp.ename
                return render(request,'first/success.html')
            else:
                messages.error(request,'enter correct username and password')
        except Employee.DoesNotExist:
            print('user does not exist')
        return redirect('/list')

def saveimg(request):
    if request.session['ename']:
        ename = request.session.get('ename')
        emp=Employee.objects.filter(ename__exact=ename).first()
        if request.method == 'POST':
            emp=Employee.objects.filter(ename__exact=ename).first()
            emp.image = request.FILES.get('img')
            emp.save()
    return render(request,'first/success.html',{'emp':emp})
