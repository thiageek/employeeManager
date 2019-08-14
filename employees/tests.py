from django.test import TestCase
from django.urls import reverse

from employees.models.departments import Department
from employees.models.employees import Employee
from employees.forms.departments import DepartmentForm
from employees.forms.employees import EmployeeForm

class EmployeeManagerTest(TestCase):

  # Models test
  
  def create_department(self, name):
    return Department.objects.create(name=name)

  def test_department_creation(self):
    department = self.create_department(name="Technology")
    
    self.assertTrue(isinstance(department, Department))
    self.assertEqual(department.name, "Technology")
    self.assertEqual(department.__str__(), department.name)

  def create_employee(self, name, email, department):
    return Employee.objects.create(name=name, email=email, department=department)

  def test_employee_creation(self):
    department = self.create_department(name="Sky")
    employee = self.create_employee(name="Steve Jobs", email="steve@apple.com", department=department)
    
    self.assertTrue(isinstance(employee, Employee))
    self.assertEqual(employee.name, "Steve Jobs")
    self.assertEqual(employee.email, "steve@apple.com")
    self.assertEqual(employee.department.name, department.name)
    self.assertEqual(employee.__str__(), employee.name)

  # Views test

  def test_employees_list_view(self):
    department = self.create_department(name="Sales")
    employee = self.create_employee(name="Elon Musk", email="elon@theboring.co", department=department)
    url = reverse('index')
    response = self.client.get(url)

    self.assertEqual(response.status_code, 200)
    self.assertIn(employee.name.encode(), response.content)
