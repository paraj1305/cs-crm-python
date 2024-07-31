from django.shortcuts import render, redirect,get_object_or_404
from superadmin.models import Client,ClientImage
from django.contrib import messages
from .forms import ClientForm,ClientImageFormSet
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required(login_url='/superadmin/login/')
def client_list(request):
    clients = Client.objects.all().order_by('-id')
    search_query = request.GET.get('search', '').strip().lower()
    location = request.GET.get('location')
    industry = request.GET.get('industry')

    if search_query:
        clients = clients.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone__icontains=search_query)
        )
    if location:
        clients = clients.filter(location__icontains=location)
    if industry:
        clients = clients.filter(industry__icontains=industry)

    locations = Client.objects.values_list('location', flat=True).distinct()
    industries = Client.objects.values_list('industry', flat=True).distinct()

    context = {
        'clients': clients,
        'filters': request.GET,
        'locations': locations,
        'industries': industries,
    }
    return render(request, 'superadmin/clients/list.html', context)

@login_required(login_url='/superadmin/login/')
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            messages.success(request, 'Client created successfully.')
            return JsonResponse({'client_id': client.id}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ClientForm()
    
    return render(request, 'superadmin/clients/form.html', {'form': form})

@login_required(login_url='/superadmin/login/')
def upload_client_images(request):
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        client = get_object_or_404(Client, id=client_id)

        # Check if there are files in the request
        if 'file' in request.FILES:
            # Process each file
            for file in request.FILES.getlist('file'):
                ClientImage.objects.create(client=client, image=file)
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'error': 'No files uploaded'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required(login_url='/superadmin/login/')
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client update successfully.')
            return JsonResponse({'client_id': client.id}, status=200) 
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ClientForm(instance=client)
    return render(request, 'superadmin/clients/form.html', {'form': form})

@login_required(login_url='/superadmin/login/')
def client_delete(request, client_id):
    """Handle the deletion of a single client."""
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        client.delete()
        messages.warning(request, 'Client deleted successfully.')
        return redirect(reverse('superadmin:client_list'))
    
    return redirect(reverse('superadmin:client_list'))

@login_required(login_url='/superadmin/login/')
def bulk_client_delete(request):
    """Handle the deletion of multiple clients."""
    if request.method == 'POST':
        client_ids = request.POST.getlist('client_ids')
        if client_ids:
            # Ensure all client IDs are integers
            client_ids = [int(client_id) for client_id in client_ids]
            Client.objects.filter(pk__in=client_ids).delete()
            messages.warning(request, 'Selected clients deleted successfully.')
        else:
            messages.warning(request, 'No clients selected for deletion.')

        return redirect(reverse('superadmin:client_list'))

    return redirect(reverse('superadmin:client_list'))

def client_detail(request,client_id):
    client=get_object_or_404(Client,pk=client_id)
    client_files=client.images.all()
    projects = client.projects.all()
    
    contex={
        'client':client,
        'client_files':client_files,
        'projects':projects
    }   
    return render(request,'superadmin/clients/client_details.html',contex)