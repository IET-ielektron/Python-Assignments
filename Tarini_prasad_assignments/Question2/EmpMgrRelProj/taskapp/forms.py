from django import forms
from .models import *


choice = Designation.objects.all().values_list('dept','dept')
ch_lst = []
for i in choice:
    ch_lst.append(i)


class EmpForm(forms.ModelForm):
    class Meta:
        model = EmployeeData
        fields = ('ename','designation','manager')
        widgets = {
            'ename': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(choices=ch_lst, attrs={'class':'form-control'}),
            'manager ': forms.TextInput(attrs={'class': 'form-control'})
        }