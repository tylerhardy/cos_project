from django import forms
from .models import Directory

class DirectoryForm(forms.ModelForm):
    """
    Needed for the Duplication of assets
    """
    class Meta:
        model = Directory
        fields = [
            'status', 'first_name','last_name','email_address','department','job_title',
            'phone_number_1', 'phone_number_2', 'location', 'website', 'notes',
            'last_visit'
        ]
        widgets = {
            'last_visit': forms.DateInput(attrs={'type': 'date'}),
        }