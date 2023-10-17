from django import forms
from .models import User

class Registationform(forms.ModelForm):
    class Meta:
        model = User
        fields =['name','email','phone','pswd']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'pswd': forms.TextInput(attrs={'class': 'form-control'}),
        }