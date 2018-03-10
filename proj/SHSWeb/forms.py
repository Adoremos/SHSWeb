from django import forms
from SHSWeb.models import Students


class studentform(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'password']
        widgets = {'password' : forms.PasswordInput} 
class loginform(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
