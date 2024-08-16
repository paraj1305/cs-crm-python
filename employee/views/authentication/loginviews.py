# employee/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from superadmin.models import Employee,Project,Task,Client,EmployeeImage
from employee.models import Leave
from .login import EmployeeLoginForm,PasswordResetForm
from django.contrib.auth.decorators import login_required
import logging
from django.db.models import Q
from employee.authentication_backends import EmployeeBackend
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)

def employee_login(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            backend = EmployeeBackend()
            user = backend.authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user, backend='employee.authentication_backends.EmployeeBackend')
                logger.info("User %s logged in successfully", email)
                
                request.session['employee_id'] = user.id
                request.session['employee_first_name'] = user.first_name
                request.session['employee_last_name'] = user.last_name
                
                # try:
                #     employee_image = EmployeeImage.objects.get(employee=user)
                #     image_url = employee_image.image.url
                # except ObjectDoesNotExist:
                #     image_url = None

                return redirect('employee:home_view')
            else:
                logger.warning("Authentication failed for user: %s", email)
                messages.error(request, 'Invalid email or password.')
        else:
            logger.warning("Form submission is invalid")
            messages.error(request, 'Invalid form submission.')
    else:
        form = EmployeeLoginForm()
        
    context = {
        'form': form,

       
    } 
    return render(request, 'employee/authentication/form.html',context)
                    
def employee_password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                employee = Employee.objects.get(email=email)
                employee.set_password(password)
                employee.has_reset_password = True
                employee.save()
                messages.success(request, 'Password reset successful. Please log in with your new password.')
                return redirect('employee:employee_login')
            except Employee.DoesNotExist:
                messages.error(request, 'Employee not found.')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordResetForm()
        
    return render(request, 'employee/authentication/password_reset.html', {'form': form})



@login_required(login_url='/login/')
def home_view(request):
    employee_id = request.session.get('employee_id')
    employee_first_name = request.session.get('employee_first_name')
    employee_last_name = request.session.get('employee_last_name')
    employee_image = request.session.get('employee_image')

    if not employee_id:
        return redirect('employee:employee_login')
    
    employee = get_object_or_404(Employee, id=employee_id)
    leaves = Leave.objects.filter(employee=employee).order_by('-id')
    
    total_leaves = 20
    used_leaves = leaves.filter(status='approved').count()
    remaining_leaves = total_leaves - used_leaves

    request.session['total_leaves'] = total_leaves
    request.session['used_leaves'] = used_leaves
    request.session['remaining_leaves'] = remaining_leaves
    
    client_count = Client.objects.count()
    employee_count = Employee.objects.count()
    project_count = Project.objects.count()
    task_count = Task.objects.count()
    
    employee = request.user
    tasks = Task.objects.filter(employee=employee)
    projects = employee.projects.order_by('deadline')[:3]


    context = {
        'employee_id': employee_id,
        'employee_first_name': employee_first_name,
        'employee_last_name': employee_last_name,
        'employee_image': employee_image,
        'client_count': client_count,
        'employee_count': employee_count,
        'project_count': project_count,
        'task_count': task_count,
        'leaves': leaves,
        'total_leaves': total_leaves,
        'used_leaves': used_leaves,
        'remaining_leaves': remaining_leaves,
        'tasks':tasks,
        'projects':projects
        
    }
    return render(request, 'employee/dashboard.html', context)

def employee_logout(request):
    if 'employee_id' in request.session:
        del request.session['employee_id']
    messages.success(request, 'Logged out successfully.')
    return redirect('employee:employee_login')

