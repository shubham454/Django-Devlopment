from django.shortcuts import render
from first.models import Student

# Create your views here.
def student_info(request):
    data = Student.objects.filter(name__iexact = 'swaPnil')
    return render(request,"first/home.html", {"data":data})
