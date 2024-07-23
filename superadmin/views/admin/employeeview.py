from django.shortcuts import render, redirect, get_object_or_404
from superadmin.models import Employee,EmployeeImage
from django.contrib import messages
from .forms import EmployeeForm
from django.urls import reverse
import secrets
import string
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/superadmin/login/')
def employee_list(request):
    employees = Employee.objects.all().order_by('-id')

    # Filtering based on search query
    search_query = request.GET.get('search_query')
    if search_query:
        employees = employees.filter(first_name__icontains=search_query) | employees.filter(last_name__icontains=search_query) | employees.filter(email__icontains=search_query)

    return render(request, 'superadmin/employees/employees.html', {'employees': employees, 'search_query': search_query})

def generate_random_password(length=10):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

@login_required(login_url='/superadmin/login/')
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                employee = form.save(commit=False)
                # Generate a random password
                random_password = generate_random_password()
                employee.set_password(random_password)
                employee.save()
                messages.success(request, 'Employee cretae successfully')
                
                # Send email with the random password
                send_mail(
                    'Your Account Password',
                    f'Hello {employee.first_name},\n\nYour account has been created. Your password is: {random_password}\n\nPlease log in and change your password immediately.',
                    'your_email@example.com',
                    [employee.email],
                    fail_silently=False,
                )
                # Return the employee ID to the client
                return JsonResponse({'employee_id': employee.id})
            except Exception as e:
                return JsonResponse({'errors': {'__all__': [str(e)]}}, status=400)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = EmployeeForm()
    return render(request, 'superadmin/employees/form.html', {'form': form})

@login_required(login_url='/superadmin/login/')
def upload_employee_images(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        employee = get_object_or_404(Employee, id=employee_id)
        files = request.FILES.getlist('file')
        for file in files:
            EmployeeImage.objects.create(employee=employee, image=file)
        return JsonResponse({'message': 'Images uploaded successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required(login_url='/superadmin/login/')
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully')
            return JsonResponse({'employee_id': employee.id})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'superadmin/employees/form.html', {'form': form})

@login_required(login_url='/superadmin/login/')
def employee_delete(request, pk):
    """Handle the deletion of a single employee."""
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.warning(request, 'Employee deleted successfully.')
        return redirect(reverse('superadmin:employee_list'))
    
    return redirect(reverse('superadmin:employee_list'))

@login_required(login_url='/superadmin/login/')
def bulk_employee_delete(request):
    """Handle the deletion of multiple employees."""
    if request.method == 'POST':
        employee_ids = request.POST.getlist('employee_ids')
        if employee_ids:
            Employee.objects.filter(pk__in=employee_ids).delete()
            messages.warning(request, 'Selected employees deleted successfully.')
        else:
            messages.warning(request, 'No employees selected for deletion.')

        return redirect(reverse('superadmin:employee_list'))

    return redirect(reverse('superadmin:employee_list'))