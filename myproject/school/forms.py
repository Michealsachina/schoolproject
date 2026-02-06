from django import forms
from .models import School

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name','address','city','state','pincode','principal_name','phone','email','established_year']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
            'established_year': forms.NumberInput(attrs={'min': 1800, 'max': 2100}),
        }
