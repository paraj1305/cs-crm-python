from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from superadmin.models import Project,Client


from django.contrib.auth.decorators import login_required

from django.db.models import Q


@login_required
def project_list(request):
    employee = request.user
    search_query = request.GET.get('search_query', '')
    client_filter = request.GET.get('client', '')
    priority_filter = request.GET.get('priority', '')
    status_filter = request.GET.get('status', '')

    if search_query:
        projects = Project.objects.filter(tasks__isnull=False).distinct()(
            Q(project_title__icontains=search_query) |
            Q(client__name__icontains=search_query)
        )
    else:
        projects = employee.projects.all().order_by('-id')
        
    if client_filter:
        projects = projects.filter(client__id=client_filter)

    if priority_filter:
        projects = projects.filter(priority=priority_filter)

    if status_filter:
        projects = projects.filter(status=status_filter)
    
    clients = Client.objects.all()
    priorities = Project.PRIORITY_LEVELS
    statuses = Project.STATUS_LEVELS
    
    context = {
       'projects': projects,
        'search_query': search_query,
        'client_filter': client_filter,
        'priority_filter': priority_filter,
        'status_filter': status_filter,
        'clients': clients,
        'priorities': priorities,
        'statuses': statuses,
    }
    return render(request, 'employee/projects/projects.html', context)

def projects(request, project_id):
    """Display detailed information about a specific project."""
    project = get_object_or_404(Project, pk=project_id)
    project_files = project.files.all()  # Fetch related project files using 'files' related name
    change_requests = project.changerequest_set.all()  # Fetch related change requests
    project_tasks = project.tasks.all()  # Fetch related tasks

    return render(request, 'employee/projects/projects_details.html', {
        'project': project,
        'change_requests': change_requests,
        'project_files': project_files,
        'project_tasks': project_tasks,
    })