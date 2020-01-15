from django.urls import path

from .views import (employee_create_view, employee_delete_view,
                    employee_edit_view, employee_list_view,
                    employee_search_view)

app_name = 'employee'
urlpatterns = [
    path("create/", employee_create_view, name='employee_create'),
    path("list/", employee_list_view, name='employee_list'),
    path("delete/<int:id>/", employee_delete_view, name='employee_delete'),
    path("edit/<int:id>/", employee_edit_view, name='employee_edit'),
    path("search/", employee_search_view, name="search")
]
