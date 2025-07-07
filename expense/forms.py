from django import forms
from .models import ExpenseModel


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseModel
        fields = ['amount', 'category', 'note']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter note'})
        }
