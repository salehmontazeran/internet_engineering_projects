# Generated by Django 3.0.2 on 2020-01-24 21:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20200115_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$', 'Only alphabetical characters are allowed.'), django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$', 'Only alphabetical characters are allowed.'), django.core.validators.MinLengthValidator(1)]),
        ),
    ]
