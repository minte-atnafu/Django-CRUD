from django import forms
from .models import Employee
# include your forms here

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('full_name','phone_number','emp_code','postion')
        labels = {
            'full_name': 'Full Name',
            'emp_code':'EMP. Code'
        }
