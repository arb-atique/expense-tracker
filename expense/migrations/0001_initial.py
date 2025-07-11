# Generated by Django 5.2.3 on 2025-07-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6, max_length=10)),
                ('category', models.CharField(choices=[('fd', 'Food'), ('tr', 'Transport'), ('en', 'Entertainment'), ('ot', 'Others')], default='ot', max_length=2)),
                ('note', models.TextField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
