# Generated by Django 4.1.5 on 2023-01-28 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tax_data',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_tax',
        ),
    ]
