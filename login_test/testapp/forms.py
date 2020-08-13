from django import forms
from testapp.models import Entry
class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields='__all__'
