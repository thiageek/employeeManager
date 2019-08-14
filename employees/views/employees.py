import json
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from ..models.employees import Employee
from ..forms.employees import EmployeeForm

def index(request):
  employees = Employee.objects.all()
  data = []
  for employee in employees:
    data.append(employee.getData())
  return httpResponseAsJson(data)

def detail(request, employee_id):
  employee = Employee.objects.get(pk=employee_id)
  return httpResponseAsJson(employee.getData())

@csrf_exempt
def add(request):
  form = EmployeeForm(request.POST)
  if(not form.is_valid()):
    errors = "Invalid parameters: " + (','.join(form.errors))
    return HttpResponseBadRequest(errors)
  employee = Employee()
  employee.setData(form)
  employee.save()
  return httpResponseAsJson(employee.getData())

@csrf_exempt
def update(request, employee_id):
  try:
    employee = Employee.objects.get(pk=employee_id)
  except Employee.DoesNotExist:
    return HttpResponseNotFound("Employee not found.")
  form = EmployeeForm(request.POST)
  if(not form.is_valid()):
    errors = "Invalid parameters: " + (','.join(form.errors))
    return HttpResponseBadRequest(errors)
  employee.setData(form)
  employee.save()
  return httpResponseAsJson(employee.getData())

def remove(request, employee_id):
  try:
    employee = Employee.objects.get(pk=employee_id)
  except Employee.DoesNotExist:
    return HttpResponseNotFound("Employee not found.")
  employee.delete()
  return redirect('index')

def httpResponseAsJson(data):
  jsonData = json.dumps(data)
  return HttpResponse(jsonData, content_type="application/json")
