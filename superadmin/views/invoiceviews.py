# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_POST
from superadmin.models import Invoice, InvoiceItem,Superadmin
from ..forms import InvoiceForm, InvoiceItemForm
from django.db.models import Sum
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
import decimal
from django.core.serializers.json import DjangoJSONEncoder


    
@login_required(login_url='/superadmin/login/')
def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.save()
            messages.success(request, 'Invoice created successfully.')

            item_data_list = []
            for key in request.POST.keys():
                if key.startswith('items[') and key.endswith('][title]'):
                    index = key.split('[')[1].split(']')[0]
                    title = request.POST[key]
                    rate = float(request.POST[f'items[{index}][rate]'])
                    item_data_list.append({'title': title, 'rate': rate})

            print('Item data list:', item_data_list) # Debugging line

            for item_data in item_data_list:
                item = InvoiceItem(
                    invoice=invoice,
                    title=item_data['title'],
                    rate=item_data['rate'],
                )
                item.save()

            return JsonResponse({'success': True, 'redirect_url': reverse('superadmin:invoice_detail', args=[invoice.id])})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = InvoiceForm()
    return render(request, 'superadmin/invoice/invoice_form.html', {'form': form})



@login_required(login_url='/superadmin/login/')
@require_POST
def add_invoice_item(request):
    form = InvoiceItemForm(request.POST)
    if form.is_valid():
        item = form.save(commit=False)
        item.invoice_id = request.POST.get('invoice_id')  # This assumes an invoice ID is available
        item.save()
        return JsonResponse({
            'success': True,
            'item': {
                'title': item.title,
                'rate': float(item.rate),
            }
        })
    return JsonResponse({'success': False, 'errors': form.errors})



from django.db.models import Q

@login_required(login_url='/superadmin/login/')
def invoice_list(request):
    payment_status = request.GET.get('payment_status')
    search_query = request.GET.get('search_query')

    invoices = Invoice.objects.all().order_by('-id')

    if payment_status:
        invoices = invoices.filter(payment_status=payment_status)
    
    if search_query:
        invoices = invoices.filter(client__name__icontains=search_query)

    return render(request, 'superadmin/invoice/invoice_list.html', {
        'invoices': invoices,
        'payment_status': payment_status,
        'search_query': search_query,
    })

@login_required(login_url='/superadmin/login/')
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    total_rate = invoice.total_amount()
    tax_amount = (invoice.tax_percentage / 100) * total_rate
    adjusted_total = total_rate + tax_amount
    
    client_invoices = Invoice.objects.filter(client=invoice.client).exclude(id=invoice_id)

    
    return render(request, 'superadmin/invoice/invoice_detail.html', {
        'invoice': invoice,
        'total_rate': total_rate,
        'tax_percentage': invoice.tax_percentage,
        'tax_amount': tax_amount,
        'adjusted_total': adjusted_total,
        'client_invoices':client_invoices
    })


class DecimalEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super().default(obj)

@login_required(login_url='/superadmin/login/')
def invoice_edit(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            invoice = form.save()
            
            # Clear existing items and add updated ones
            invoice.items.all().delete()
            
            items = []
            item_data_list = []
            for key in request.POST.keys():
                if key.startswith('items[') and key.endswith('][title]'):
                    index = key.split('[')[1].split(']')[0]
                    title = request.POST[key]
                    rate = float(request.POST[f'items[{index}][rate]'])
                    item_data_list.append({'title': title, 'rate': rate})
            
            for item_data in item_data_list:
                item = InvoiceItem(
                    invoice=invoice,
                    title=item_data['title'],
                    rate=item_data['rate'],
                )
                item.save()
                items.append(item)

            messages.success(request, 'Invoice updated successfully.')
            return JsonResponse({'success': True, 'redirect_url': reverse('superadmin:invoice_detail', args=[invoice.id])})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = InvoiceForm(instance=invoice)

    invoice_items = list(invoice.items.all().values('title', 'rate'))
    invoice_items_json = json.dumps(invoice_items, cls=DecimalEncoder)
    
    return render(request, 'superadmin/invoice/invoice_form.html', {
        'form': form, 
        'invoice': invoice, 
        'invoice_items_json': invoice_items_json
    })

@login_required(login_url='/superadmin/login/')
def invoice_delete(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == 'POST':
        invoice.delete()
        messages.warning(request, 'invoice delete successfully.')
        return redirect('superadmin:invoice_list')
    return render(request, 'superadmin/invoice/invoice_confirm_delete.html', {'invoice': invoice})

@login_required(login_url='/superadmin/login/')
def invoice_item_create(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == 'POST':
        form = InvoiceItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.invoice = invoice
            item.save()
            return redirect('superadmin:invoice_detail', invoice_id=invoice.id)
    else:
        form = InvoiceItemForm()
    return render(request, 'superadmin/invoice/invoice_item_form.html', {'form': form})

@login_required(login_url='/superadmin/login/')
def invoice_item_delete(request, invoice_id, item_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    item = get_object_or_404(InvoiceItem, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('superadmin:invoice_detail', invoice_id=invoice.id)
    return render(request, 'superadmin/invoice/invoice_item_confirm_delete.html', {'item': item})



import io
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.db.models import Sum
from django.templatetags.static import static
from django.contrib import messages
from django.core.mail import EmailMessage

def generate_invoice_pdf(invoice):
    # Fetch items related to the invoice
    items = invoice.items.all()
    superadmin = Superadmin.objects.first()

    # Calculate total rate from items
    total_rate = items.aggregate(total_rate=Sum('rate'))['total_rate'] or 0

    # Example fixed tax percentage and calculations
    tax_percentage = 10
    tax_amount = (total_rate * tax_percentage) / 100
    adjusted_total = total_rate + tax_amount

    # Context for rendering the HTML template
    context = {
        'invoice': invoice,
        'items': items,
        'total_rate': total_rate,
        'tax_percentage': tax_percentage,
        'tax_amount': tax_amount,
        'adjusted_total': adjusted_total,
        'superadmin': superadmin,
        'logo_url': static('images/coderscotch-logo.png'),  # Adjust as per your static file setup
    }

    # Render HTML template as a string
    html_string = render_to_string('superadmin/invoice/invoice_pdf.html', context)

    # Create a PDF object
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html_string.encode("UTF-8")), result, encoding="UTF-8")

    if pdf.err:
        # Handle error if PDF generation fails
        print(f'Error creating PDF for invoice #{invoice.id}: {pdf.err}')
        return None

    # Close the result object
    pdf_data = result.getvalue()
    result.close()

    return pdf_data

@login_required(login_url='/superadmin/login/')
def send_invoice_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    
    # Generate PDF
    pdf_data = generate_invoice_pdf(invoice)

    if pdf_data:
        # Example: Email the PDF to the client
        client_email = invoice.client.email
        email = EmailMessage(
            subject=f'Invoice #{invoice.id}',
            body='Please find attached your invoice.',
            to=[client_email],
        )
        email.attach(f'invoice_{invoice.id}.pdf', pdf_data, 'application/pdf')
        email.send()

        # Optional: Update invoice sent_to_client status
        invoice.sent_to_client = True
        invoice.save()

        # Pass a success message to the template
        message = 'Invoice sent successfully!'
    else:
        message = 'Failed to generate PDF.'

    return render(request, 'superadmin/invoice/invoice_detail.html', {'invoice': invoice, 'message': message})


@login_required(login_url='/superadmin/login/')
def download_invoice_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)

    # Generate PDF
    pdf_data = generate_invoice_pdf(invoice)

    if pdf_data:
        response = HttpResponse(pdf_data, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.id}.pdf"'
        return response
    else:
        messages.error(request, 'Failed to generate PDF.')
        return redirect('superadmin:invoice_detail', invoice_id=invoice.id)