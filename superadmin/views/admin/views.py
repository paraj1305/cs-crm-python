# accounts/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from superadmin.models import Superadmin,Client,Employee,Project,Task,Lead
from .forms import LoginForm,SuperadminForm
from django.contrib.auth import logout
from superadmin.models import Client
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login


from django.contrib.auth import authenticate, login

def login_view(request):
    form = LoginForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Authenticate user
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                # Login user if authentication succeeds
                login(request, user)
                company_name = request.session.get('company_name')
                request.session['company_name'] = user.company_name
                # Redirect to the appropriate page after login
                return redirect(reverse('superadmin:home'))  # Adjust 'superadmin:home' to your actual URL name
            else:
                # Display error message if authentication fails
                messages.error(request, 'Invalid email or password.')
            
            context = {
                'company_name':company_name,
                'form':form
            }
    
    # Render the login form page with form context
    
    return render(request, 'superadmin/login.html', {'context': context})


@login_required(login_url='/superadmin/login/')
def admin_profile(request):
    # Get the email of the logged-in user
    user_email = request.user.email.lower()
    print(f"Logged-in user's email: {user_email}")

    # Fetch the Superadmin profile using case-insensitive comparison
    try:
        superadmin = Superadmin.objects.get(email__iexact=user_email)
    except Superadmin.DoesNotExist:
        return redirect('superadmin:login')
        return HttpResponse("Superadmin profile not found for this email.")

    return render(request, 'superadmin/profile/profile.html', {'superadmin': superadmin})

def edit_superadmin(request):
    superadmin = request.user  # Assuming the logged-in user is the superadmin being edited
    
    if request.method == 'POST':
        form = SuperadminForm(request.POST, request.FILES, instance=superadmin)
        if form.is_valid():
            form.save()
            return redirect(reverse('superadmin:home'))
    else:
        form = SuperadminForm(instance=superadmin)
        
    
    
    return render(request, 'superadmin/profile/superadminform.html', {'form': form})


@login_required(login_url='/superadmin/login/')
def home_view(request):
    client_count = Client.objects.count()
    employee_count = Employee.objects.count()
    project_count = Project.objects.count()
    task_count = Task.objects.count()
    lead_count = Lead.objects.count()
    company_name = request.session.get('company_name')
    
    
    

    

    context = {
        'client_count': client_count,
        'employee_count': employee_count,
        'project_count': project_count,
        'task_count': task_count,
        'lead_count':lead_count,
        'company_name': company_name,
       
    }
    return render(request, 'superadmin/dashboard.html', context)

   

def logout_view(request):
    # Clear the session data to log out the user
    request.session.flush()  # This removes all session data
    messages.success(request, "You have been logged out successfully.")
    
    # Redirect to the login page
    return redirect(reverse('superadmin:login')) 