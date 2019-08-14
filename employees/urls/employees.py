from django.urls import path

from ..views import employees

urlpatterns = [
  path('', employees.index, name='index'),
  path('<int:employee_id>', employees.detail, name='detail'),
  path('add', employees.add, name='add'),
  path('update/<int:employee_id>', employees.update, name='update'),
  path('remove/<int:employee_id>', employees.remove, name='remove')
]
