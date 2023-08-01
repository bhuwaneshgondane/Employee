from django import forms
from .models import EmployeeM


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeM
        fields = "__all__"
