# Generated by Django 4.1.5 on 2023-01-10 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_staff',
        ),
    ]