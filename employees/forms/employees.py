from django import forms
from django.forms import ModelForm

from ..models.employees import Employee
from ..models.departments import Department

class EmployeeForm(ModelForm):
  department = forms.ModelChoiceField(queryset=Department.objects.all())
  class Meta:
    model = Employee
    fields = ['name', 'email', 'department']
