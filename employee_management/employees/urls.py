from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),  # The employee list view
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),  # Add this linepath('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),  # Add this line
     path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]