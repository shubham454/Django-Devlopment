from django.shortcuts import render
from first.models import Dog

# Create your views here.
def all_dog(request):
    data = Dog.objects.all()
    return render(request, "first/home.html",{'data':data})

def value(request):
    data = Dog.objects.all().values('name')
    return render(request, "first/home.html",{'data':data})

def lt_method(request):
    data = Dog.objects.filter(cost__lt = 9000)
    return render(request, "first/home.html",{'data':data})

def gt_method(request):
    data = Dog.objects.filter(cost__gt = 9000)
    return render(request, "first/home.html",{'data':data})

def in_method(request):
    data = Dog.objects.filter(name__in = ['xyz','abc','bulldog'])
    return render(request, "first/home.html",{'data':data})

def count(request):
    data = Dog.objects.all().count()
    return render(request, "first/home.html",{'data':data})
