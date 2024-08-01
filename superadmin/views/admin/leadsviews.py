from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from superadmin.models import Lead,LeadFile
from .forms import LeadForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
import logging

@login_required(login_url='/superadmin/login/')
def lead_list(request):
    search_query = request.GET.get('search_query', '')
    location_filter = request.GET.get('location', '')

    leads = Lead.objects.all().order_by('-id')

    if search_query:
        leads = leads.filter(
            Q(project_name__icontains=search_query) | 
            Q(company__icontains=search_query) | 
            Q(email__icontains=search_query)
        )

    if location_filter:
        leads = leads.filter(location__icontains=location_filter)

    locations = Lead.objects.values_list('location', flat=True).distinct()

    return render(request, 'superadmin/leads/leads.html', {
        'leads': leads,
        'search_query': search_query,
        'location_filter': location_filter,
        'locations': locations,
    })

@login_required(login_url='/superadmin/login/')
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    lead_files = lead.files.all()  # Fetch related lead files

    # Print lead files to the terminal
    for file in lead_files:
        print(f"File Name: {file.file.name}, File URL: {file.file.url}")

    return render(request, 'superadmin/leads/leaddetail.html', {'lead': lead,})

logger = logging.getLogger(__name__)

@login_required(login_url='/superadmin/login/')
def lead_create(request):
    form = LeadForm(request.POST or None, files=request.FILES or None)
    
    if request.method == 'POST':
        if form.is_valid():
            try:
                lead = form.save()

                # Save uploaded files
                if 'file' in request.FILES:
                    for file in request.FILES.getlist('file'):
                        LeadFile.objects.create(lead=lead, file=file)

                messages.success(request, 'Lead created successfully.')
                return JsonResponse({'lead_id': lead.pk}, status=200)
                
            except Exception as e:
                logger.error(f'An error occurred while creating the lead: {str(e)}', exc_info=True)
                messages.error(request, f'An error occurred while creating the lead: {str(e)}')
                return JsonResponse({'errors': str(e)}, status=500)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = LeadForm()

    return render(request, 'superadmin/leads/createlead.html', {'form': form})

@login_required(login_url='/superadmin/login/')
def upload_lead_filess(request):
    if request.method == 'POST':
        lead_id = request.POST.get('lead_id')
        lead = get_object_or_404(Lead, id=lead_id)

        # Check if there are files in the request
        if 'file' in request.FILES:
            # Process each file
            for file in request.FILES.getlist('file'):
                LeadFile.objects.create(lead=lead, file=file)  # Assuming 'file' is the correct field name
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'error': 'No files uploaded'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required(login_url='/superadmin/login/')
def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Lead updated successfully.')
            return JsonResponse({'lead_id': lead.pk, 'message': 'Lead created successfully.'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = LeadForm(instance=lead)
    return render(request, 'superadmin/leads/createlead.html', {'form': form})


@login_required
def lead_delete(request, lead_id):
    """Handle the deletion of a single lead."""
    lead = get_object_or_404(Lead, pk=lead_id)
    if request.method == 'POST':
        lead.delete()
        messages.warning(request, 'Lead deleted successfully.')
        return redirect(reverse('superadmin:lead_list'))
    
    return redirect(reverse('superadmin:lead_list'))

@login_required
def bulk_lead_delete(request):
    """Handle the deletion of multiple leads."""
    if request.method == 'POST':
        lead_ids = request.POST.getlist('lead_ids')
        if lead_ids:
            Lead.objects.filter(pk__in=lead_ids).delete()
            messages.warning(request, 'Selected leads deleted successfully.')
        else:
            messages.warning(request, 'No leads selected for deletion.')

        return redirect(reverse('superadmin:lead_list'))

    return redirect(reverse('superadmin:lead_list'))