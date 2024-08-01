from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from employee.models import Leave
from superadmin.models import Employee
from .leaves.form import LeaveForm


def apply_leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = request.user  # Set the employee to the current user
            leave.save()
            return redirect('employee:home_view')  # Adjust with your actual URL name
    else:
        form = LeaveForm()
    
    return render(request, 'employee/leaves/apply_leave.html', {'form': form})

@login_required
def leaves(request):
    employee = request.user

    # Filter leaves by the current employee
    leaves = Leave.objects.filter(employee=employee).order_by('-id')
    total_leaves = 20
    used_leaves = leaves.filter(status='approved').count()
    remaining_leaves = total_leaves - used_leaves

    context = {
        'leaves': leaves,
        'total_leaves': total_leaves,
        'used_leaves': used_leaves,
        'remaining_leaves': remaining_leaves,
    }
    return render(request, 'employee/leaves/leaves.html', context)
   

