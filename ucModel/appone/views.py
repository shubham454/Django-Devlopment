from django.shortcuts import render, redirect
from appone.forms import *
from appone.models import *

# Create your views here.
def index_view(request):
    form = UniForm()
    form1 = ColForm()
    return render(request,"appone/index.html",{'form':form,"form1":form1})

def add_uni(request):
    form = UniForm()
    if request.method == "POST":
        form = UniForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/appone/index/')

def add_col(request):
    form1 = ColForm()
    if request.method == "POST":
        form = ColForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/appone/index/')

def show_colg(request):
    form = ColForm()
    if request.method == "POST":
        nm = request.POST.get('uname')
        data = Col.objects.get(uname__uname = nm)
        return render(request, 'appone/colg.html',{'form':form,'data':data})

def show_uni(request):
    if request.method == "POST":
        nm = request.POST.get('cname')
        data = Uni.objects.get(col__cname = nm )
        return render(request,'appone/uni.html',{'data':data})
