from django.shortcuts import render, redirect, get_object_or_404
from superadmin.models import Employee,EmployeeImage,SalarySlip,Superadmin,Task,Project
from django.contrib import messages
from .forms import EmployeeForm,SalarySlipForm
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
    salary_slip = SalarySlip.objects.all()
    
    
    
    # Filtering based on search query
    search_query = request.GET.get('search_query')
    if search_query:
        employees = employees.filter(first_name__icontains=search_query) | employees.filter(last_name__icontains=search_query) | employees.filter(email__icontains=search_query)

    return render(request, 'superadmin/employees/employees.html', {'employees': employees, 'search_query': search_query,'salary_slip':salary_slip})

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

def employee_detail(request,employee_id):
    employee=get_object_or_404(Employee,pk=employee_id)
    employee_images=employee.images.all()
    tasks = Task.objects.filter(employee=employee)
    employees = Employee.objects.all()
    
    
    contex={
        'employee':employee,
        'employee_images':employee_images,   
        'tasks':tasks,
        'employees': employees,
    }
    return render(request,'superadmin/employees/employee_details.html',contex)

@login_required(login_url='/superadmin/login/')
def project_tasks(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    # tasks = project.tasks.all()
    tasks = Task.objects.filter(project=project, employee__id=request.GET.get('employee_id', None))

    return render(request, 'superadmin/employees/project_tasks.html', {
        'project': project,
        'tasks': tasks,
    })

def check_or_create_salary_slip(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    salary_slip = SalarySlip.objects.filter(employee=employee).order_by('-year', '-month').first()
    
    if salary_slip:
        return redirect('superadmin:salary_slip_detail', salary_slip_id=salary_slip.id)
    else:
        return redirect('superadmin:create_salary_slip', employee_id=employee.id)

def create_salary_slip(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    previous_salary_slips = SalarySlip.objects.filter(employee=employee).order_by('-year', '-month')
    
    if request.method == 'POST':
        form = SalarySlipForm(request.POST)
        if form.is_valid():
            salary_slip = form.save(commit=False)
            salary_slip.employee = employee
            salary_slip.save()
            return redirect(reverse('superadmin:salary_slip_detail', args=[salary_slip.id]))
    else:
        form = SalarySlipForm()
    
    return render(request, 'superadmin/employees/create_salary_slip.html', {
        'form': form,
        'employee': employee,
        'previous_salary_slips': previous_salary_slips,
        'form_action': reverse('superadmin:create_salary_slip', args=[employee.id]),
        'form_title': 'Create',
        'button_text': 'Create Salary Slip'
    })

def update_salary_slip(request, salary_slip_id):
    salary_slip = get_object_or_404(SalarySlip, pk=salary_slip_id)
    previous_salary_slips = SalarySlip.objects.filter(employee=salary_slip.employee).order_by('-year', '-month')
    
    if request.method == 'POST':
        form = SalarySlipForm(request.POST, instance=salary_slip)
        if form.is_valid():
            form.save()
            return redirect(reverse('superadmin:salary_slip_detail', args=[salary_slip.id]))
    else:
        form = SalarySlipForm(instance=salary_slip)
    
    return render(request, 'superadmin/employees/create_salary_slip.html', {
        'form': form,
        'employee': salary_slip.employee,
        'previous_salary_slips': previous_salary_slips,
        'form_action': reverse('superadmin:update_salary_slip', args=[salary_slip.id]),
        'form_title': 'Update',
        'button_text': 'Update Salary Slip'
    })

def salary_slip_detail(request, salary_slip_id):
    salary_slip = get_object_or_404(SalarySlip, id=salary_slip_id)
    superadmin = Superadmin.objects.first()
    previous_salary_slips = SalarySlip.objects.filter(employee=salary_slip.employee).exclude(id=salary_slip_id)

    context = {
        'salary_slip': salary_slip,
        'superadmin': superadmin,
        'previous_salary_slips': previous_salary_slips,
    }
    return render(request, 'superadmin/employees/salary_slip_detail.html', context)

def delete_salary_slip(request, salary_slip_id):
    salary_slip = get_object_or_404(SalarySlip, pk=salary_slip_id)
    employee_id = salary_slip.employee.id
    salary_slip.delete()
    return redirect(reverse('superadmin:create_salary_slip', args=[employee_id]))

import io
from xhtml2pdf import pisa
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse


def generate_salary_slip_pdf(request, salary_slip_id):
    salary_slip = get_object_or_404(SalarySlip, id=salary_slip_id)
    superadmin = Superadmin.objects.first()
    html_string = render_to_string('superadmin/employees/salary_slip.html', {'salary_slip': salary_slip,'superadmin':superadmin})
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html_string.encode("UTF-8")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=salary_slip_{salary_slip_id}.pdf'
        return response
    return HttpResponse('We had some errors <pre>' + html_string + '</pre>')