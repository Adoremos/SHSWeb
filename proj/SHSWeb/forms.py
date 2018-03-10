from django import forms
from SHSWeb.models import Students


class studentform(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'password']
        widgets = {'password' : forms.PasswordInput} 