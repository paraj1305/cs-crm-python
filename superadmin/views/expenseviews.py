from superadmin.models import Expense
from ..forms import ExpenseForm
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.contrib import messages
import calendar
from datetime import datetime
from django.db.models import Q 

def expense_list(request):
    search_query = request.GET.get('search', '')


    # Start with all expenses
    expenses = Expense.objects.all().order_by('-date')

    # Filter based on search query if provided
    if search_query:
        expenses = expenses.filter(
            Q(category__icontains=search_query) |
            Q(description__icontains=search_query)
        )

 

    context = {
        'expenses': expenses,
    
    }

    return render(request, 'superadmin/expenses/expense_list.html', context)


# def add_or_update_expense(request, pk=None):
#     if pk:
#         expense = get_object_or_404(Expense, pk=pk)
#         form = ExpenseForm(request.POST or None, instance=expense)
#     else:
#         expense = None
#         form = ExpenseForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('superadmin:expense_list')

#     return render(request, 'superadmin/expenses/add_expense.html', {'form': form, 'expense': expense})

def add_or_update_expense(request, pk=None):
    if pk:
        expense = get_object_or_404(Expense, pk=pk)
        form = ExpenseForm(request.POST or None, instance=expense)
    else:
        expense = None
        form = ExpenseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('superadmin:expense_list')

    return render(request, 'superadmin/expenses/add_expense.html', {'form': form, 'expense': expense})



# Delete view
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('superadmin:expense_list')