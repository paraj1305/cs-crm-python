# accounts/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from superadmin.models import Superadmin,Client,Employee,Project,Task,Lead
from .forms import LoginForm,SuperadminForm,ReportFilterForm
from django.contrib.auth import logout
from superadmin.models import Client,Invoice,SalarySlip
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from django.db.models import Sum, F,Q, ExpressionWrapper, DecimalField
from django.contrib.auth import authenticate, login
from django.utils.timezone import now
import json


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
                
                request.session['company_name'] = user.company_name
               
                # Redirect to the appropriate page after login
                return redirect(reverse('superadmin:home'))  # Adjust 'superadmin:home' to your actual URL name
            else:
                # Display error message if authentication fails
                messages.error(request, 'Invalid email or password.')
    
    # Render the login form page with form context
    context = {
        'form': form,
   
    }
    
    return render(request, 'superadmin/login.html', context)


@login_required(login_url='/superadmin/login/')
def admin_profile(request):
    user_email = request.user.email.lower()
    try:
        superadmin = Superadmin.objects.get(email__iexact=user_email)
    except Superadmin.DoesNotExist:
        return redirect('superadmin:login')

    company_name = request.user.company_name
    context = {
        'superadmin': superadmin,
        'company_name': company_name,
    }

    return render(request, 'superadmin/profile/profile.html', context)

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

def get_filtered_total_revenue(year=None, month=None):
    try:
        filters = {'payment_status': 'paid'}
        if year and year != 'yearly':
            filters['invoice_date__year'] = year
        if month:
            filters['invoice_date__month'] = month
        
        paid_invoices = Invoice.objects.filter(**filters)
        total_revenue = paid_invoices.annotate(
            total_amount_with_tax=Sum(F('items__rate') + (F('items__rate') * F('tax_percentage') / 100))
        ).aggregate(
            total_revenue=Sum('total_amount_with_tax')
        )['total_revenue'] or 0
        return total_revenue
    except Exception as e:
        print(f"Error calculating total revenue: {e}")
        return 0
    


from django.db.models import F, Sum, ExpressionWrapper, DecimalField, Q

def get_total_cost_and_salary(year=None, month=None):
    try:
        filters = Q()
        if year and year != 'yearly':
            filters &= Q(year=year)
        if month:
            filters &= Q(month=month)

        total_salary = SalarySlip.objects.filter(filters).aggregate(
            total=Sum(
                ExpressionWrapper(
                    F('employee__salary') - 
                    (F('employee__salary') * (F('professional_tax') / 100)) - 
                    (F('employee__salary') * (F('TDS') / 100)) - 
                    F('leave_deduction'),
                    output_field=DecimalField()
                )
            )
        )['total'] or 0

        total_company_salary = SalarySlip.objects.aggregate(
            total=Sum(
                ExpressionWrapper(
                    F('employee__salary') - 
                    (F('employee__salary') * (F('professional_tax') / 100)) - 
                    (F('employee__salary') * (F('TDS') / 100)) - 
                    F('leave_deduction'),
                    output_field=DecimalField()
                )
            )
        )['total'] or 0

        return round(total_salary, 2), round(total_company_salary, 2)
    except Exception as e:
        print(f"Error calculating total cost and salary: {e}")
        return 0, 0


import json

def generate_chart_data(year=None, month=None):
    # Default labels for months
    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Fixed range of years
    start_year = 2010
    end_year = 2024
    year_labels = list(range(start_year, end_year + 1))
    
    revenue_data = []
    cost_data = []
    profit_data = []
    goal_data = [2000] * len(year_labels)  # Example goal value, adjust as needed

    if year == 'yearly':
        # Handle yearly data within the fixed range
        for y in year_labels:
            filters = Q(payment_status='paid') & Q(invoice_date__year=y)
            paid_invoices = Invoice.objects.filter(filters)
            total_revenue = paid_invoices.annotate(
                total_amount_with_tax=Sum(F('items__rate') + (F('items__rate') * F('tax_percentage') / 100))
            ).aggregate(
                total_revenue=Sum('total_amount_with_tax')
            )['total_revenue'] or 0

            total_cost, _ = get_total_cost_and_salary(y, None)
            total_profit = total_revenue - total_cost

            # Append data for each year
            revenue_data.append(float(total_revenue))
            cost_data.append(float(total_cost))
            profit_data.append(float(total_profit))

        labels = year_labels
    else:
        # Handle monthly data for a specific year
        if year:
            labels = month_labels
            for m in range(1, 13):
                filters = Q(payment_status='paid')
                if year and year != 'yearly':
                    filters &= Q(invoice_date__year=year)
                if month:
                    filters &= Q(invoice_date__month=month)
                else:
                    filters &= Q(invoice_date__month=m)
                
                paid_invoices = Invoice.objects.filter(filters)
                total_revenue = paid_invoices.annotate(
                    total_amount_with_tax=Sum(F('items__rate') + (F('items__rate') * F('tax_percentage') / 100))
                ).aggregate(
                    total_revenue=Sum('total_amount_with_tax')
                )['total_revenue'] or 0

                total_cost, _ = get_total_cost_and_salary(year, m)
                total_profit = total_revenue - total_cost

                # Convert Decimal to float
                revenue_data.append(float(total_revenue))
                cost_data.append(float(total_cost))
                profit_data.append(float(total_profit))
                goal_data.append(1500)  # Example goal value, adjust as needed
        else:
            labels = month_labels

    chart_data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Revenue',
                'data': revenue_data,
                'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Cost',
                'data': cost_data,
                'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Profit',
                'data': profit_data,
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Goal',
                'data': goal_data,
                'backgroundColor': 'rgba(255, 206, 86, 0.2)',
                'borderColor': 'rgba(255, 206, 86, 1)',
                'borderWidth': 1
            }
        ]
    }

    return json.dumps(chart_data)



@login_required(login_url='/superadmin/login/')
def home_view(request):
    form = ReportFilterForm(request.GET or None)

    # If the form is not valid or the year is not provided, set default to 'yearly'
    if form.is_valid():
        year = form.cleaned_data.get('year') if form.cleaned_data.get('year') else 'yearly'
        month = form.cleaned_data.get('month') if form.cleaned_data.get('month') else None
        chart_type = form.cleaned_data.get('chart_type') if form.cleaned_data.get('chart_type') else 'bar'
    else:
        year = 'yearly'
        month = None
        chart_type = 'bar'

    client_count = Client.objects.count()
    employee_count = Employee.objects.count()
    project_count = Project.objects.count()
    task_count = Task.objects.count()
    lead_count = Lead.objects.count()

    total_cost, total_company_salary = get_total_cost_and_salary(year, month)
    total_revenue = get_filtered_total_revenue(year, month)
    total_profit = total_revenue - total_cost

    chart_data = generate_chart_data(year, month)
    nearest_deadline_projects = Project.objects.filter(status='inprogress').order_by('deadline')[:3]
    latest_leads = Lead.objects.order_by('-id')[:3]
    last_tasks = Task.objects.order_by('-due_date')[:3]
    last_unpaid_invoices = Invoice.objects.filter(payment_status='unpaid').order_by('-invoice_date')[:3]
    
    context = {
        'client_count': client_count,
        'employee_count': employee_count,
        'project_count': project_count,
        'task_count': task_count,
        'lead_count': lead_count,
        'total_revenue': total_revenue,
        'total_cost': total_cost,
        'total_company_salary': total_company_salary,
        'total_profit': total_profit,
        'form': form,
        'chart_data': chart_data,
        'chart_type': chart_type,
        'nearest_deadline_projects': nearest_deadline_projects,
        'latest_leads': latest_leads,
        'last_tasks': last_tasks,
        'last_unpaid_invoices': last_unpaid_invoices
    }
    return render(request, 'superadmin/dashboard.html', context)


    
def logout_view(request):
    # Clear the session data to log out the user
    # request.session.flush()  # This removes all session data
    messages.success(request, "You have been logged out successfully.")
    
    # Redirect to the login page
    return redirect(reverse('superadmin:login')) 