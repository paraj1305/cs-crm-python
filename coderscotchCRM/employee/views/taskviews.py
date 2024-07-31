from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from superadmin.models import Task,Client
from django.db.models import Q 

@login_required
def employee_tasks(request):
    employee = request.user
    search_query = request.GET.get('search_query', '')
    priority_filter = request.GET.get('priority', '')
    status_filter = request.GET.get('status', '')

    tasks = Task.objects.filter(employee=employee)

    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) | Q(project__project_title__icontains=search_query)
        )
    
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)
    
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    
    clients = Client.objects.all()
 
    
    context = {
        'tasks': tasks,
        'search_query': search_query,
        'priority_filter': priority_filter,
        'status_filter': status_filter,
        'priorities': Task.PRIORITY_CHOICES,
        'statuses': Task.STATUS_CHOICES,
        'clients':clients,
    }
    return render(request, 'employee/tasks/tasks.html', context)



@login_required
def task_detail(request, task_id):
    # Get the task object by id
    task = get_object_or_404(Task, pk=task_id, employee=request.user)

    context = {
        'task': task
    }
    return render(request, 'employee/tasks/task_detail.html', context)