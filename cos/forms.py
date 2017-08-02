from django import forms
from django.forms.models import ModelForm
from .models import Asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_tag', 'computer_name', 'equipment_role', 'equipment_condition', 'inventory_system', 'inventory_system_current', 'user', 'curator', 'department', 'org_code', 'location', 'vendor', 'vendor_serial_number', 'purchase_order', 'purchase_date', 'purchase_cost', 'funded_by', 'hardware_type', 'hardware_make', 'hardware_model', 'hardware_serial_number', 'network_connection', 'ip_address', 'mac_wired', 'mac_wireless', 'processor', 'harddrive', 'ram', 'graphics', 'os', 'os_arch', 'active_directory', 'organizational_unit', 'sccm', 'jamf', 'scep', 'identity_finder', 'notes']

class AssetCreateForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_tag', 'computer_name', 'equipment_role', 'equipment_condition', 'inventory_system', 'inventory_system_current', 'user', 'curator', 'department', 'org_code', 'location', 'vendor', 'vendor_serial_number', 'purchase_order', 'purchase_date', 'purchase_cost', 'funded_by', 'hardware_type', 'hardware_make', 'hardware_model', 'hardware_serial_number', 'network_connection', 'ip_address', 'mac_wired', 'mac_wireless', 'processor', 'harddrive', 'ram', 'graphics', 'os', 'os_arch', 'active_directory', 'organizational_unit', 'sccm', 'jamf', 'scep', 'identity_finder', 'notes']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }