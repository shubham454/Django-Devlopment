from django.shortcuts import render, redirect
from first.models import Student
from first.forms import StudentForm
from django.views import View

# Create your views here.
def all_view(request):
    data = Student.objects.all()
    return render(request,"first/home.html",{'data':data})

def add_view(request):
    form = StudentForm(request.POST or None)
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            marks = form.cleaned_data.get('marks')
            email = form.cleaned_data.get('email')
            print(name,marks,email)
            obj = Student.objects.create(name = name, marks = marks, email = email)
    return render(request,'first/add.html',{'form':form})


class Name(View):
    def get(self,request):
        return render(request, 'first/one.html')

    def post(self,request):
        return render(request, 'first/two.html')
