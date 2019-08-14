from django.db import models

class Department(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def setData(self, data):
    self.name = data.cleaned_data['name']

  def getData(self):
    from .employees import Employee
    employees = Employee.objects.get(department_id=self.id)
    return {
      'id': self.id,
      'name': self.name,
      'employees': employees.getData()
    }

