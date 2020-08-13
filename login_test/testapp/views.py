from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from testapp.models import Entry
from testapp.forms import EntryForm
from testapp.decorators import user_is_entry_author

@login_required
def index(request):
    entries=Entry.objects.filter(created_by=request.user)
    return render(request,'testapp/index.html',{'entries':entries})

@login_required
def add(request):
    if request.method=='POST':
        form=EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Entry was successfully added!')
            return redirect('index')
    form=EntryForm()
    return render(request,'testapp/entry.html',{'form':form})

@login_required
@user_is_entry_author
def edit(request,id):
    entry=get_object_or_404(Entry,pk=id)
    if request.method=='POST':
        form=EntryForm(request.POST,instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request,'Entry was successfully added!')
            return redirect('index')
    form=EntryForm(instance=entry)
    return render(request,'testapp/entry.html',{'form':form})
