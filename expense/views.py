from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .forms import ExpenseForm
from . import views
from .models import ExpenseModel
# Create your views here.


def homepage(request):
    expenses = ExpenseModel.objects.all()
    # total = sum(expense.amount for expense in expenses)
    total = ExpenseModel.objects.aggregate(total=Sum('amount'))['total'] or 0
    # ExpenseModel.objects.aggregate(total=Sum('amount'))['total'] or 0
    return render(request, 'expense/index.html', {
        'expenses': expenses,
        'total': total
    })


def create_expense(request):
    expenses = ExpenseModel.objects.all()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ExpenseForm()
    return render(request, 'expense/create_expense.html', {
        'form': form,
        'expenses': expenses
    })


def edit_expense(request, pk):
    expense = get_object_or_404(ExpenseModel, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense/create_expense.html', {'form': form, 'is_instance': expense is not None})


def delete_expense(request, pk):
    expense = get_object_or_404(ExpenseModel, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('homepage')
    return render(request, 'expense/confirm_delete.html', {
        'expense': expense
    })
