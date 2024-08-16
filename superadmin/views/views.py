# accounts/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from superadmin.models import Superadmin,Client,Employee,Project,Task,Lead
from ..forms import LoginForm,SuperadminForm,ReportFilterForm
from django.contrib.auth import logout
from superadmin.models import Client,Invoice,SalarySlip
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from django.db.models import Sum, F,Q,Count, ExpressionWrapper, DecimalField
from django.contrib.auth import authenticate, login
from django.utils.timezone import now
import json
from datetime import datetime
from django import forms

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
                return redirect(reverse('superadmin:home')) 
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
    superadmin = request.user  
    
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
    goal_data = [40000] * len(year_labels)  # Example goal value, adjust as needed

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
                goal_data.append(15000)  # Example goal value, adjust as needed
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


def get_second_chart_data(year2=None, month2=None):
    # Define filter conditions
    filter_conditions = {}
    if year2:
        filter_conditions['invoice_date__year'] = year2
    if month2:
        filter_conditions['invoice_date__month'] = month2

        # Query the database for invoice data
    try:
        second_chart_data = (
            Invoice.objects
            .filter(**filter_conditions)
            .values('client__name')
            .annotate(
                paid_total=Sum(
                    F('items__rate') * (1 + F('tax_percentage') / 100),
                    filter=Q(payment_status='paid')
                ),
                unpaid_total=Sum(
                    F('items__rate') * (1 + F('tax_percentage') / 100),
                    filter=Q(payment_status='unpaid')
                ),
                paid_count=Count('id', distinct=True, filter=Q(payment_status='paid')),
                unpaid_count=Count('id', distinct=True, filter=Q(payment_status='unpaid')),
            )
            .order_by('-paid_total', '-unpaid_total')
        )
    except Exception as e:
        print(f"Error fetching invoice data: {e}")
        second_chart_data = []

    # Extract labels and data for the chart
    second_chart_labels = [item['client__name'] for item in second_chart_data]
    second_chart_paid_data = [float(item['paid_total'] or 0) for item in second_chart_data]
    second_chart_unpaid_data = [float(item['unpaid_total'] or 0) for item in second_chart_data]
    paid_invoices_count = sum(item['paid_count'] for item in second_chart_data)
    unpaid_invoices_count = sum(item['unpaid_count'] for item in second_chart_data)
    paid_invoices_amount = sum(float(item['paid_total'] or 0) for item in second_chart_data)
    unpaid_invoices_amount = sum(float(item['unpaid_total'] or 0) for item in second_chart_data)

    # Structure the data for the chart
    second_chart_json = json.dumps({
        'labels': second_chart_labels,
        'datasets': [
            {
                'label': 'Paid Invoices (Total Amount)',
                'data': second_chart_paid_data,
                'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Unpaid Invoices (Total Amount)',
                'data': second_chart_unpaid_data,
                'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            }
        ]
    })

    return {
        'chart_data': second_chart_json,
        'paid_invoices_count': paid_invoices_count,
        'unpaid_invoices_count': unpaid_invoices_count,
        'paid_invoices_amount': paid_invoices_amount,
        'unpaid_invoices_amount': unpaid_invoices_amount
    }


@login_required(login_url='/superadmin/login/')
def home_view(request):
    form = ReportFilterForm(request.GET or None)
    
    # Set default values for year, month, and chart type
    year = 'yearly'
    month = None
    chart_type = 'bar'
    
    # Update values if the form is valid
    if form.is_valid():
        year = form.cleaned_data.get('year') or year
        month = form.cleaned_data.get('month')
        chart_type = form.cleaned_data.get('chart_type') or chart_type

    # Fetch total counts
    client_count = Client.objects.count()
    employee_count = Employee.objects.count()
    project_count = Project.objects.count()
    task_count = Task.objects.count()
    lead_count = Lead.objects.count()

    # Calculate costs, revenue, and profit
    total_cost, total_company_salary = get_total_cost_and_salary(year, month)
    total_revenue = get_filtered_total_revenue(year, month)
    total_profit = total_revenue - total_cost

    # Generate chart data
    chart_data = generate_chart_data(year, month)

    # Get projects with nearest deadlines
    nearest_deadline_projects = Project.objects.filter(status='inprogress').order_by('deadline')[:3]
    
    # Get the latest leads and tasks
    latest_leads = Lead.objects.order_by('-id')[:3]
    last_tasks = Task.objects.order_by('-due_date')[:3]

    # Get the last unpaid invoices
    last_unpaid_invoices = Invoice.objects.filter(payment_status='unpaid').order_by('-invoice_date')[:3]
    
    # Filters for the second chart
    year2 = request.GET.get('year2')
    month2 = request.GET.get('month2')
    
    # Get the chart data with filters
    second_chart_data = get_second_chart_data(year2=year2, month2=month2)
    
    # Extract data from the second chart data
    second_chart_json = second_chart_data['chart_data']
    paid_invoices_count = second_chart_data['paid_invoices_count']
    unpaid_invoices_count = second_chart_data['unpaid_invoices_count']
    paid_invoices_amount = second_chart_data['paid_invoices_amount']
    unpaid_invoices_amount = second_chart_data['unpaid_invoices_amount']

    # Get current year for year range
    current_year = datetime.now().year
    years = range(2015, current_year + 1)
    months = [
        {'value': 1, 'name': 'January'},
        {'value': 2, 'name': 'February'},
        {'value': 3, 'name': 'March'},
        {'value': 4, 'name': 'April'},
        {'value': 5, 'name': 'May'},
        {'value': 6, 'name': 'June'},
        {'value': 7, 'name': 'July'},
        {'value': 8, 'name': 'August'},
        {'value': 9, 'name': 'September'},
        {'value': 10, 'name': 'October'},
        {'value': 11, 'name': 'November'},
        {'value': 12, 'name': 'December'},
    ]

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
        'last_unpaid_invoices': last_unpaid_invoices,
        'second_chart_data': second_chart_json,
        'paid_invoices_count': paid_invoices_count,
        'unpaid_invoices_count': unpaid_invoices_count,
        'paid_invoices_amount': paid_invoices_amount,
        'unpaid_invoices_amount': unpaid_invoices_amount,
        'year': year,
        'month': month,
        'year2': year2,
        'month2': month2,
        'years': years,
        'months': months,
    }
    return render(request, 'superadmin/dashboard.html', context)


    
def logout_view(request):
    # Clear the session data to log out the user
    # request.session.flush()  # This removes all session data
    messages.success(request, "You have been logged out successfully.")
    
    # Redirect to the login page
    return redirect(reverse('superadmin:login')) 