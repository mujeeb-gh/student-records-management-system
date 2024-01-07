from django import forms
from .models import Student
from bootstrap_datepicker_plus.widgets import DatePickerInput


class StudentForm(forms.ModelForm):
  class Meta:
      model = Student
      fields = ['matric_number', 'full_name', 'passport_photo', 'department', 'college', 'cgpa', 'gender', 'age', 'date_of_birth', 'contact_no', 'address', 'email', 'nationality', 'state']
      
      widgets = {
            'date_of_birth': DatePickerInput(),
        }
