from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from first.forms import User_registrationForm
from first.models import Image
# import for messaging sysytem
from django.contrib import messages

# Create your views here.
def User_registration(request):
    form = User_registrationForm()
    if request.method == 'POST':
        form = User_registrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'user registered successfully{user}')
            return render(request, 'first/register.html',{'form':form})
    return render(request,'first/register.html',{"form":form})

def success_view(request):
    obj = Image.objects.all()
    return render(request,'first/success.html',{'obj':obj})
