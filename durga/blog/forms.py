from django import forms
class EmailSendForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=Flase,widget=forms.Textarea)
