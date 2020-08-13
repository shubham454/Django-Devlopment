from django import forms
from .models import ItemAdd

class ItemAddForm(forms.ModelForm):
    class Meta:
        model = ItemAdd
        fields = '__all__'
