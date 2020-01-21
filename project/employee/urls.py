from django.urls import path

from .views import (delete_users_on_gender, employee_create_view,
                    employee_delete_view, employee_edit_view,
                    employee_list_view, employee_report_view,
                    employee_search_view, get_users_with_name,
                    update_user_salary)

app_name = 'employee'
urlpatterns = [
    path("create/", employee_create_view, name='employee_create'),
    path("list/", employee_list_view, name='employee_list'),
    path("delete/<int:id>/", employee_delete_view, name='employee_delete'),
    path("edit/<int:id>/", employee_edit_view, name='employee_edit'),
    path("search/", employee_search_view, name="search"),
    path("report/", employee_report_view),
    path("myget/<str:name>/", get_users_with_name),
    path("myupdate/<int:personal_number>/<int:salary>/", update_user_salary),
    path("mydel/<str:gender>/", delete_users_on_gender)
]
