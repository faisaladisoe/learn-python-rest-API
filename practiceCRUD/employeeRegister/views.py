from django.shortcuts import render, redirect
from .forms import EmployeeForm, PositionForm
from .models import Employee, Position

# Create your views here.
def employee_list(request):
    content = {
        'employeeList' : Employee.objects.all()
    }
    return render(request, 'employeeRegister/employeeList.html', content)

def employee_form(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(instance = employee)
            content = {
                'form' : form
            }
        return render(request, 'employeeRegister/employeeForm.html', content)
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(request.POST, instance = employee)
            
        if form.is_valid():
            form.save()
        return redirect('/list/')

def employee_delete(request):
    return