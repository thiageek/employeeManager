from django.contrib import admin

from .models.employees import Employee
from .models.departments import Department

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
