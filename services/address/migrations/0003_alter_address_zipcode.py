# Generated by Django 4.1.5 on 2023-01-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_alter_address_address_alter_address_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.CharField(max_length=255),
        ),
    ]