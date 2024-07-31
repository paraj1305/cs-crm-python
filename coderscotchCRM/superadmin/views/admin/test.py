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
                if year:
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
