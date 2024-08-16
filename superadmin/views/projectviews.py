# superadmin/views/admin/projectviews.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from superadmin.models import Project, ChangeRequest,ProjectFile,Task
from ..forms import ProjectForm, ChangeRequestForm
import logging
from django.http import JsonResponse
from superadmin.models import Client
from django.db.models import Q


@login_required(login_url='/superadmin/login/')
def project_list(request):
    search_query = request.GET.get('search_query', '')
    client_filter = request.GET.get('client', '')
    priority_filter = request.GET.get('priority', '')
    status_filter = request.GET.get('status', '')

    projects = Project.objects.all().order_by('-id')

    if search_query:
        projects = projects.filter(
            Q(project_title__icontains=search_query) |
            Q(client__name__icontains=search_query)
        )

    if client_filter:
        projects = projects.filter(client__id=client_filter)

    if priority_filter:
        projects = projects.filter(priority=priority_filter)

    if status_filter:
        projects = projects.filter(status=status_filter)

    clients = Client.objects.all()
    priorities = Project.PRIORITY_LEVELS
    statuses = Project.STATUS_LEVELS

    return render(request, 'superadmin/projects/projects.html', {
        'projects': projects,
        'search_query': search_query,
        'client_filter': client_filter,
        'priority_filter': priority_filter,
        'status_filter': status_filter,
        'clients': clients,
        'priorities': priorities,
        'statuses': statuses,
    })
    
    
# Set up logging
logger = logging.getLogger(__name__)

@login_required(login_url='/superadmin/login/')
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                project = form.save(commit=False)
                project.assigned_to = request.user
                project.save()

                selected_employees = form.cleaned_data.get('employees')
                if selected_employees:
                    project.employees.set(selected_employees)


                messages.success(request, 'Project created successfully.')
                
            except Exception as e:
                logger.error(f'An error occurred while creating the project: {str(e)}', exc_info=True)
                messages.error(request, f'An error occurred while creating the project: {str(e)}')
            return JsonResponse({'project_id': project.id}, status=200)
        else:
            messages.error(request, 'There were errors in the form. Please correct them and try again.')
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ProjectForm()

    return render(request, 'superadmin/projects/project_form.html', {'form': form})

@login_required(login_url='/superadmin/login/')
def upload_project_filess(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        project = get_object_or_404(Project, id=project_id)

        # Check if there are files in the request
        if 'file' in request.FILES:
            # Process each file
            for file in request.FILES.getlist('file'):
                ProjectFile.objects.create(project=project, file=file)  # Assuming 'file' is the correct field name
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'error': 'No files uploaded'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required(login_url='/superadmin/login/')
def project_update(request, project_id):
    """Handle updating an existing project."""
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully.')
            return JsonResponse({'project_id': project.id}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'superadmin/projects/project_form.html', {'form': form})

@login_required(login_url='/superadmin/login/')
def project_delete(request, project_id):
    """Handle the deletion of a single project."""
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.delete()
        messages.warning(request, 'Project deleted successfully.')
        return redirect(reverse('superadmin:project_list'))
    
    return redirect(reverse('superadmin:project_list'))

@login_required(login_url='/superadmin/login/')
def bulk_project_delete(request):
    """Handle the deletion of multiple projects."""
    if request.method == 'POST':
        project_ids = request.POST.getlist('project_ids')
        if project_ids:
            Project.objects.filter(pk__in=project_ids).delete()
            messages.warning(request, 'Selected projects deleted successfully.')
        else:
            messages.warning(request, 'No projects selected for deletion.')

        return redirect(reverse('superadmin:project_list'))

    return redirect(reverse('superadmin:project_list'))


@login_required(login_url='/superadmin/login/')
def change_request_create(request, project_id):
    """Handle adding a change request to a project."""
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ChangeRequestForm(request.POST)
        if form.is_valid():
            change_request = form.save(commit=False)
            change_request.project = project
            change_request.save()
            messages.success(request, 'Change request added successfully.')
            
            # Redirect to the project's detail page using reverse with kwargs
            return redirect(reverse('superadmin:project_detail', kwargs={'project_id': project.id}))
    else:
        form = ChangeRequestForm(initial={'project': project})
    
    return render(request, 'superadmin/projects/change_request_form.html', {'form': form})

@login_required(login_url='/superadmin/login/')
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project_files = project.files.all()  # Fetch related project files
    change_requests = project.changerequest_set.all()
    tasks = Task.objects.filter(project=project)

    context = {
        'project': project,
        'project_files': project_files,
        'change_requests':change_requests,
        'tasks':tasks
    }
    return render(request, 'superadmin/projects/project_detail.html', context)
