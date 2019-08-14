from django import forms
from django.forms import ModelForm

from ..models.departments import Department

class DepartmentForm(ModelForm):
  class Meta:
    model = Department
    fields = ['name']
