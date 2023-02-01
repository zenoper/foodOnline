# Generated by Django 4.1.5 on 2023-01-27 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_openhours'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openhours',
            options={'ordering': ('day', '-from_hour')},
        ),
        migrations.AlterUniqueTogether(
            name='openhours',
            unique_together={('vendor', 'day', 'from_hour', 'to_hour')},
        ),
    ]