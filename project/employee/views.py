from statistics import stdev

from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min, Sum
from django.forms import ValidationError
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from .forms import ChnageEmployeeForm, EmployeeForm
from .models import Employee
from .serializers import EmployeeSerializer


@login_required
def employee_create_view(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employee:employee_list')

    context = {
        'form': form
    }
    return render(request, "employee/employee_create.html", context)


@login_required
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


@login_required
def employee_delete_confirmation_view(request, id):
    obj = Employee.objects.filter(id=id)
    if not obj:
        return render(request, 'employee/employee_notfound.html')
    if request.method == "POST":
        if request.POST['action'] == "Delete":
            obj.delete()
        return redirect('employee:employee_list')

    context = {
        "object": obj[0]
    }
    return render(
        request,
        "employee/employee_delete_confirmation.html",
        context
    )


@login_required
def employee_delete_view(request):
    if request.method == "POST":
        personal_number = request.POST.get('personal_number')
        print("*** ", personal_number)
        obj = Employee.objects.filter(personal_number=personal_number)
        if not obj:
            return render(request, 'employee/employee_notfound.html')
        obj.delete()

    return render(request, 'employee/employee_delete.html')


@login_required
def employee_edit_view(request, id):
    obj = Employee.objects.filter(id=id)
    if not obj:
        return render(request, 'employee/employee_notfound.html')

    form = ChnageEmployeeForm(request.POST or None, instance=obj[0])
    if form.is_valid():
        form.save()
        return redirect('employee:employee_list')

    context = {
        'form': form
    }
    return render(request, "employee/employee_create.html", context)


@login_required
def employee_search_view(request):
    return render(request, 'employee/employee_search.html')


def extract_employee_description(employee):
    return (
            f"Name: {employee.first_name} {employee.last_name}  "
            f"SSN: {employee.ssn}  "
            f"Personal number: {employee.personal_number}"
    )


@login_required
def employee_report_view(request):

    try:

        total_single = (Employee.objects.
                        filter(marital_status__exact="Single").count())
        total_married = (Employee.objects.
                         filter(marital_status__exact="Married").count())

        salary_more_1000000 = (Employee.objects.
                               filter(salary__gt=1000000).count())

        temp = Employee.objects.aggregate(
            Max('salary'),
            Min('salary'),
            Sum('salary')
        )
        max_salary = temp["salary__max"]
        min_salary = temp["salary__min"]
        sum_salary = temp["salary__sum"]

        max_salary_emp = Employee.objects.get(salary=max_salary)
        max_salary_employee_info = extract_employee_description(
            max_salary_emp
        )

        min_salary_emp = Employee.objects.get(salary=min_salary)
        min_salary_employee_info = extract_employee_description(
            min_salary_emp
        )

        salary_list = Employee.objects.values_list('salary', flat=True)
        if len(salary_list) < 2:
            salary_stdev = 0
        else:
            salary_stdev = stdev(salary_list)

        context = {
            "total_single": total_single,
            "total_married": total_married,
            "salary_more_1000000": salary_more_1000000,
            "max_salary_employee_info": max_salary_employee_info,
            "min_salary_employee_info": min_salary_employee_info,
            "sum_salary": sum_salary,
            "salary_stdev": salary_stdev,
        }
    except Exception as e:
        print(e)
        return render(request, "employee/employee_report_error.html")

    return render(request, "employee/employee_report.html", context)


@api_view(['GET'])
def get_users_with_name(request, name):
    employees = Employee.objects.filter(first_name__exact=name)
    return Response(EmployeeSerializer(employees, many=True).data)


@api_view(['POST'])
def update_user_salary(request, personal_number, salary):
    affected_rows = Employee.objects.filter(personal_number=personal_number) \
                    .update(salary=salary)
    return Response({"affected rows": affected_rows})


@api_view(['DELETE'])
def delete_users_on_gender(request, gender):
    if gender == "male" or gender == "female":
        affected_rows = Employee.objects.filter(gender__iexact=gender) \
                                        .delete()
        return Response({"affected rows": affected_rows[0]})
    else:
        return Response(status=HTTP_404_NOT_FOUND)


@login_required
def home_page(request):
    return render(request, "base.html")


@login_required
def user_logout(request):
    logout(request)
    return redirect('home_page')
