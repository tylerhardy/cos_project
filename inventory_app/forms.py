from django import forms
from .models import Asset

class AssetForm(forms.ModelForm):
    """
    Needed for the Duplication of assets
    """
    class Meta:
        model = Asset
        fields = [
            'asset_tag', 'inventory_system', 'hardware_name', 'location',
            'vendor', 'vendor_serial_number', 'hardware_type', 'hardware_make',
            'hardware_model', 'hardware_serial_number', 'network_connection',
            'ip_address', 'mac_wired', 'mac_wireless', 'processor',
            'harddrive', 'ram', 'graphics', 'os', 'os_arch', 'user', 'curator',
            'hardware_role', 'hardware_condition', 'department', 'org_code',
            'requisition_number', 'purchase_order', 'purchase_date',
            'purchase_cost', 'eligible_upgrade', 'eligible_upgrade_date',
            'funded_by', 'active_directory', 'organizational_unit', 'sccm',
            'jamf', 'scep', 'identity_finder', 'notes', 'audited_date',
            ]

        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'audited_date': forms.DateInput(attrs={'type': 'date'}),
        }