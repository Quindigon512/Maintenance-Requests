from django import forms
from .models import Request

class MaintenanceRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['aptNum', 'area', 'descr', 'image']
