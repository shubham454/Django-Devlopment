from django.shortcuts import render, redirect
from .models import BankAccount
from django.views.generic import View
from first.forms import BankAccountForm


# Create your views here.
class GetBankData(View):
    def get(self, request):
        bankaccount = BankAccount.objects.all().order_by('-ano')
        return render(request, 'first/list.html', {'bankaccount': bankaccount})


class AddBankData(View):
    def get(self, request):
        form = BankAccountForm()
        return render(request, 'first/add.html', {'form': form})

    def post(self, request):
        form = BankAccountForm(request.POST)
        if form.is_valid():
            ano = form.cleaned_data.get('ano')
            name = form.cleaned_data.get('name')
            add = form.cleaned_data.get('add')
            obj = BankAccount(ano=ano, name=name, add=add)
            obj.save()
            return redirect('/list')
        return render(request, 'first/add.html',{'form':form})


class DeleteView(View):
    def get(self, request, ano):
        obj = BankAccount.objects.filter(ano=ano)
        obj.delete()
        return redirect('/list')

class UpdateView(View):
    def get(self,request,ano):
        obj = BankAccount.objects.get(ano=ano)
        form = BankAccountForm()
        return render(request,'first/update.html',{'form':form,'obj':obj})
