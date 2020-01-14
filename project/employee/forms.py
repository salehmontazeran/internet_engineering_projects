from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    ssn = forms.CharField(
        label='SSN',
        max_length=10,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    personal_number = forms.CharField(
        max_length=7,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    mobile = forms.CharField(
        max_length=11,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    address = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}
        )
    )
    marital_status = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=Employee.MARITAL_STATUS
        )
    )
    gender = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=Employee.GENDER
        )
    )
    age = forms.IntegerField(
        max_value=70,
        min_value=18,
        widget=forms.NumberInput(
            attrs={'class': 'form-control'},
        )
    )
    salary = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control'},
        )
    )

    class Meta:
        model = Employee
        fields = "__all__"
