from django.core.validators import (MaxLengthValidator, MaxValueValidator,
                                    MinLengthValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

numerical = RegexValidator(r'^[0-9]*$', 'Only numerical characters are allowed.')
alphabetical = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetical characters are allowed.')
mobile = RegexValidator(r'^09\d{9}$', 'Only valid mobile number is allowed.')


class Employee(models.Model):
    MARITAL_STATUS = [
        ('Single', 'Single'),
        ('Married', 'Married')
    ]

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    first_name = models.CharField(
        max_length=30,
        validators=[alphabetical, MinLengthValidator(1)]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[alphabetical, MinLengthValidator(1)]
    )
    ssn = models.CharField(
        max_length=10,
        validators=[numerical, MinLengthValidator(10), MaxLengthValidator(10)]
    )
    personal_number = models.CharField(
        max_length=7,
        validators=[numerical, MinLengthValidator(7), MaxLengthValidator(7)]
    )
    mobile = models.CharField(
        max_length=11,
        validators=[mobile]
    )
    address = models.TextField()
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS)
    gender = models.CharField(max_length=10, choices=GENDER)
    age = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(70)]
    )
    salary = models.PositiveIntegerField()
