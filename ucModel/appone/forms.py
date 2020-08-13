from django import forms
from appone.models import *

class UniForm(forms.ModelForm):
    class Meta:
        model = Uni
        fields = "__all__"

class ColForm(forms.ModelForm):
    class Meta:
        model = Col
        fields = "__all__"
