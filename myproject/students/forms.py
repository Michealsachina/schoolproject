from django import forms
from .models import Student
from django.core.exceptions import ValidationError
from datetime import date

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'dob', 'photo', 'email', 'student_class', 'grade', 'school']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'school': forms.HiddenInput(),
        }

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob and dob > date.today():
            raise ValidationError("Date of birth cannot be in the future.")
        return dob
