from django import forms
from django.core import validators

class DateInput(forms.DateInput):
    input_type='date'
class BankAccountForm(forms.Form):
    ano = forms.IntegerField()
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    add = forms.CharField(max_length=50,validators=[validators.MaxLengthValidator(10)])
    date = forms.DateField(widget=DateInput(attrs={'class':'form-control'}))

    def clean_ano(self):
        inputano = self.cleaned_data['ano']
        if inputano < 100:
            raise forms.ValidationError('Acoount number should be start from 100')
        return inputano

    def clean_name(self):
        inputname = self.cleaned_data['name']
        if len(inputname) <= 3:
            raise forms.ValidationError('please enter valid name, name should be greater than 3 lettersS')
        return inputname
