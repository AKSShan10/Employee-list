from django.shortcuts import render, redirect  # Add redirect to the imports
from .models import Employee
from .forms import EmployeeForm  # Import EmployeeForm
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.core.paginator import Paginator


# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to the employee list after successful submission
    else:
        form = EmployeeForm()

    return render(request, 'employees/add_employee.html', {'form': form})


def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/edit_employee.html', {'form': form, 'employee': employee})


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/delete_employee.html', {'employee': employee})


def delete_employee(request, employee_id):
    # Retrieve the employee based on the ID, or show a 404 error if not found
    employee = get_object_or_404(Employee, id=employee_id)

    # If the request method is POST, delete the employee
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')  # Redirect back to the employee list after deletion

    # If GET request, render the delete confirmation page
    return render(request, 'employees/delete_employee.html', {'employee': employee})


# def employee_list(request):
#     query = request.GET.get('search', '')
#     sort_by = request.GET.get('sort', 'first_name')  # Default sorting by first_name

#     # Search functionality
#     employees = Employee.objects.filter(
#         Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)
#     ).order_by(sort_by)

#     return render(request, 'employees/employee_list.html', {'employees': employees, 'search_query': query, 'sort_by': sort_by})


# def employee_list(request):
#     query = request.GET.get('search', '')
#     sort_by = request.GET.get('sort', 'first_name')  # Default sorting by first_name

#     # Search functionality
#     employees = Employee.objects.filter(
#         Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)
#     ).order_by(sort_by)

#     return render(request, 'employees/employee_list.html', {'employees': employees, 'search_query': query, 'sort_by': sort_by})


# def employee_list(request):
#     query = request.GET.get('search', '')
#     sort_by = request.GET.get('sort', 'first_name')

#     employees = Employee.objects.filter(
#         Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)
#     ).order_by(sort_by)

#     # Pagination
#     paginator = Paginator(employees, 10)  # Show 10 employees per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'employees/employee_list.html', {'page_obj': page_obj, 'search_query': query, 'sort_by': sort_by})


def employee_list(request):
    search_name_query = request.GET.get('search_name', '')
    search_email_query = request.GET.get('search_email', '')
    sort_by = request.GET.get('sort', 'first_name')

    # Filtering by search query for name or email
    employees = Employee.objects.all()
    if search_name_query != '':
        if search_email_query != '':
            employees = employees.filter(
                Q(first_name__icontains=search_name_query) |
                Q(last_name__icontains=search_name_query) |
                Q(email__icontains=search_email_query)
            )
        else:
            employees = employees.filter(
                Q(first_name__icontains=search_name_query) |
                Q(last_name__icontains=search_name_query)
            )
    elif search_email_query != '':
        employees = employees.filter(
            Q(email__icontains=search_email_query)
        )

    # Sorting
    employees = employees.order_by(sort_by)

    # Pagination
    paginator = Paginator(employees, 10)  # Show 10 employees per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employees/employee_list.html', {
        'page_obj': page_obj,
        'search_name_query': search_name_query,
        'search_email_query': search_email_query,

        'sort_by': sort_by,
    })
