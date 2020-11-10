from django import forms
from django.forms import ModelForm
from .models import Employee, Position

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
    
class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = '__all__'