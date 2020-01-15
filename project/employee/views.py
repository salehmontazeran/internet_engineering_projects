from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ChnageEmployeeForm, EmployeeForm
from .models import Employee


def employee_create_view(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee:employee_list')

    context = {
        'form': form
    }
    return render(request, "employee/employee_create.html", context)


def employee_list_view(request):
    we_have_filter = False
    employee = Employee.objects

    last_name = request.GET.get('last_name')
    if last_name is not None and last_name:
        print('*** ', last_name)
        we_have_filter = True
        employee = employee.filter(last_name__exact=last_name)

    age = request.GET.get('age')
    if age is not None and age:
        we_have_filter = True
        age = int(age)
        employee = employee.filter(age=age)

    marital_status = request.GET.get('marital_status')
    if marital_status is not None and marital_status:
        we_have_filter = True
        employee = employee.filter(marital_status__exact=marital_status)

    if not we_have_filter:
        employee = employee.all()

    context = {
        'objects': employee
    }
    return render(request, "employee/employee_list.html", context)


def employee_delete_view(request, id):
    obj = get_object_or_404(Employee, id=id)
    print(obj)
    if request.method == "POST":
        if request.POST['action'] == "Delete":
            obj.delete()
        return redirect('employee:employee_list')
    context = {
        "object": obj
    }
    return render(request, "employee/employee_delete.html", context)


def employee_edit_view(request, id):
    obj = get_object_or_404(Employee, id=id)

    form = ChnageEmployeeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('employee:employee_list')

    context = {
        'form': form
    }
    return render(request, "employee/employee_create.html", context)


def employee_search_view(request):
    return render(request, 'employee/employee_search.html')


def home_page(request):
    return render(request, "base.html")
