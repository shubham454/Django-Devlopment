from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_page_view(request):
    return render(request,'first/home.html')

@login_required
def java_exam_view(request):
    return render(request,'first/javaexam.html')

@login_required
def python_exam_view(request):
    return render(request,'first/pythonexam.html')

@login_required
def aptitude_exam_view(request):
    return render(request,'first/aptitudeexam.html')

def logout_view(request):
    return render(request,'first/logout.html')
