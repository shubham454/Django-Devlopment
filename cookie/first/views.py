from django.shortcuts import render
from .models import ItemAdd
from .forms import ItemAddForm
# Create your views here.
def index(request):
    return render(request,'first/home.html')

def additem(request):
    form = ItemAddForm()
    response = render(request,'first/add.html',{'form':form})
    if request.method == 'POST':
        form = ItemAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name,quantity)
    return response

def displayitem(request):
    return render(request,'first/dispaly.html')
