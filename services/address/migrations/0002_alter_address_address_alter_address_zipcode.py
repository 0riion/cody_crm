# Generated by Django 4.1.5 on 2023-01-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
