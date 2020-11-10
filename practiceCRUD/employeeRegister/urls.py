from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employeeForm'),
    path('<int:id>/', views.employee_form, name='employeeUpdate'),
    path('list/', views.employee_list, name='employeeList'),
    path('list/delete/', views.employee_delete, name='employeeDelete'),
]