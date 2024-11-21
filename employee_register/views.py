from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee

def employee_list(request):
    # Retrieve all Employee objects
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'employee_register/employee_list.html', context)

def employee_form(request, id=0):
    if request.method == "GET": 
        if id == 0:  # For creating a new employee
            form = EmployeeForm()
        else:  # For editing an existing employee
            employee = get_object_or_404(Employee, pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_register/employee_form.html', {'form': form})
    
    else:  # Handle POST request
        if id == 0:  # Creating a new employee
            form = EmployeeForm(request.POST)
        else:  # Editing an existing employee
            employee = get_object_or_404(Employee, pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Use named URL for redirection
        return render(request, 'employee_register/employee_form.html', {'form': form})

def employee_delete(request,id):
    # Handle deletion of an employee
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')  
