from django.db import models

from .departments import Department

class Employee(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=50)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)

  def setData(self, data):
    self.name = data.cleaned_data['name']
    self.email = data.cleaned_data['email']
    self.department = data.cleaned_data['department']

  def getData(self):
    return {
      'name': self.name,
      'email': self.email,
      'department': self.department.name
    }

  def __str__(self):
    return self.name
