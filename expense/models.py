from django.db import models


# Create your models here.
class ExpenseModel(models.Model):
    category_choices = [
        ('fd', 'Food'),
        ('tr', 'Transport'),
        ('en', 'Entertainment'),
        ('ot', 'Others')
    ]
    amount = models.DecimalField(
        max_length=10, decimal_places=2, max_digits=6)
    category = models.CharField(
        max_length=2, choices=category_choices, default='ot')
    note = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)
