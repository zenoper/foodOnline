# Generated by Django 4.1.5 on 2023-02-01 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0006_alter_openhours_options_and_more'),
        ('orders', '0009_remove_order_vendors'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor.vendor'),
        ),
    ]
