from django.shortcuts import render

from .forms import EmployeeForm


def employee_create_view(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "employee/employee_create.html", context)
