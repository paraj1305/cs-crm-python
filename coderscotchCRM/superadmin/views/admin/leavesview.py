from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from superadmin.models import Leave, LeaveAdmin

@login_required(login_url='/superadmin/login/')
def leave_management(request, leave_id=None):
    # Fetch all leaves that are not approved or cancelled
    all_leaves = Leave.objects.exclude(status__in=['approved', 'cancelled'])

    # Check if a specific leave is being managed
    leave = None
    employee_name = None
    if leave_id:
        leave = get_object_or_404(Leave, id=leave_id)
        employee = leave.employee  # Assuming 'employee' is the related user object
        employee_name = f"{employee.first_name} {employee.last_name}"  # Adjust as per your User model's fields

        if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'approve':
                leave.status = 'approved'
                LeaveAdmin.objects.create(leave=leave, approved_at=timezone.now())
            elif action == 'cancel':
                leave.status = 'cancelled'
            leave.save()
            return redirect('superadmin:leave_list')  # Redirect to the leave list after action

    return render(request, 'superadmin/leaves/leave_list.html', {
        'leave': leave,
        'employee_name': employee_name,
        'all_leaves': all_leaves
    })
