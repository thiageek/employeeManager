from django.urls import path

from ..views import departments

urlpatterns = [
  path('', departments.index, name='index'),
  path('<int:department_id>', departments.detail, name='detail'),
  path('add', departments.add, name='add'),
  path('<slug:department_name>', departments.detail, name='detail'),
  path('update/<int:department_id>', departments.update, name='update'),
  path('remove/<int:department_id>', departments.remove, name='remove')
]
