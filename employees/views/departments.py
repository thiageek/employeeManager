import json
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from ..models.departments import Department
from ..forms.departments import DepartmentForm

def index(request):
  departments = Department.objects.all()
  data = []
  for department in departments:
    data.append(department.getData())
  return httpResponseAsJson(data)

def detail(request, department_id=None, department_name=None):
  query = Q(pk=department_id) | Q(name=department_name)
  try:
    department = Department.objects.get(query)
  except Department.DoesNotExist:
    return HttpResponseNotFound("Department not found.")
  return httpResponseAsJson(department.getData())

@csrf_exempt
def add(request):
  form = DepartmentForm(request.POST)
  if(not form.is_valid()):
    errors = "Invalid parameters: " + (','.join(form.errors))
    return HttpResponseBadRequest(errors)
  department = Department()
  department.setData(form)
  department.save()
  return httpResponseAsJson(department.getData())

@csrf_exempt
def update(request, department_id):
  try:
    department = Department.objects.get(pk=department_id)
  except Department.DoesNotExist:
    return HttpResponseNotFound("Department not found.")
  form = DepartmentForm(request.POST)
  if(not form.is_valid()):
    errors = "Invalid parameters: " + (','.join(form.errors))
    return HttpResponseBadRequest(errors)
  department.setData(form)
  department.save()
  return httpResponseAsJson(department.getData())

def remove(request, department_id):
  try:
    department = Department.objects.get(pk=department_id)
  except Department.DoesNotExist:
    return HttpResponseNotFound("Department not found.")
  department.delete()
  return redirect('index')

def httpResponseAsJson(data):
  jsonData = json.dumps(data)
  return HttpResponse(jsonData, content_type="application/json")
