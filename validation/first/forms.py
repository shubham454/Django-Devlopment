from django import forms


class StudentForm(forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField()
    email = forms.EmailField()


    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <= 5:
            raise forms.ValidationError('this is invalid name please length on name must be greater than 5')
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if '.edu' in email:
            raise forms.ValidationError('We do not accept educational email')
        return email

    def clean_address(self):
        l = ['ahmadnagar','nagpur','pune','mumbai', 'chandrapur','yavatmad']
        address = self.cleaned_data['address']
        if address not in l:
            raise forms.ValidationError('We do not accept other address')
        return address
