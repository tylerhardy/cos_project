from django import forms
from .models import Asset

class AssetForm(forms.ModelForm):
    """
    Needed for the Duplication of assets
    """
    class Meta:
        model = Asset
        fields = [
            'asset_tag', 'hardware_name', 'hardware_serial_number',
            'vendor_serial_number', 'hardware_role', 'hardware_condition',
            'inventory_system', 'inventory_system_current', 'user', 'curator',
            'department', 'org_code', 'location', 'vendor', 'purchase_order',
            'purchase_date', 'purchase_cost', 'funded_by', 'hardware_type',
            'hardware_make', 'hardware_model', 'network_connection',
            'ip_address', 'mac_wired', 'mac_wireless', 'processor',
            'harddrive', 'ram', 'graphics', 'os', 'os_arch',
            'active_directory', 'organizational_unit', 'sccm', 'jamf', 'scep',
            'identity_finder', 'notes'
            ]
class AssetCreateForm(forms.ModelForm):
    """
    Needed for the Creation of assets with widgets
    """
    class Meta:
        model = Asset
        fields = [
            'asset_tag', 'hardware_name', 'hardware_serial_number',
            'vendor_serial_number', 'hardware_role', 'hardware_condition',
            'inventory_system', 'inventory_system_current', 'user', 'curator',
            'department', 'org_code', 'location', 'vendor', 'purchase_order',
            'purchase_date', 'purchase_cost', 'funded_by', 'hardware_type',
            'hardware_make', 'hardware_model', 'network_connection',
            'ip_address', 'mac_wired', 'mac_wireless', 'processor',
            'harddrive', 'ram', 'graphics', 'os', 'os_arch',
            'active_directory', 'organizational_unit', 'sccm', 'jamf', 'scep',
            'identity_finder', 'notes'
            ]
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }