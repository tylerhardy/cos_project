# from django import forms
# from .models import Asset,ComputerObject

# class AssetForm(forms.ModelForm):
#     class Meta:
#         model = Asset
#         fields = [
#             'asset_tag',
#             'pc_lifecycle',
#             'property_control',
#             'user',
#             'curator',
#             'department',
#             'org_code',
#             'location',
#             'vendor',
#             'vendor_serial_number',
#             'purchase_order',
#             'purchase_date',
#             'purchase_cost',
#             'funded_by',
#             'hardware_type',
#             'hardware_make',
#             'hardware_model',
#             'hardware_serial_number',
#             'mac_wired',
#             'mac_wireless',
#             'processor',
#             'harddrive',
#             'ram',
#             'graphics',
#             'notes'
#         ]
#     def clean_asset_tag(self):
#         asset_tag = self.cleaned_data.get('asset_tag')
#         for objects in Asset.objects.all():
#             if (objects.asset_tag == asset_tag):
#                 raise forms.ValidationError('This asset tag is already in the system at location {0}'.format(objects.location))
    
#     def clean_hardware_serial_number(self):
#         hardware_serial_number = self.cleaned_data.get('hardware_serial_number')
#         for objects in Asset.objects.all():
#             if (objects.hardware_serial_number == hardware_serial_number):
#                 raise forms.ValidationError('This hardware serial number is already assigned to {0}'.format(objects.asset_tag))
#         return hardware_serial_number

#     def clean_vendor_serial_number(self):
#         vendor_serial_number = self.cleaned_data.get('vendor_serial_number')
#         for objects in Asset.objects.all():
#             if (objects.vendor_serial_number == vendor_serial_number):
#                 raise forms.ValidationError('This vendor serial number is already assigned to {0}'.format(objects.asset_tag))
#         return vendor_serial_number

# class ComputerObjectForm(forms.ModelForm):
#     class Meta:
#         model = ComputerObject
#         fields = [
#             'computer_name',
#             'os_arch',
#             'os',
#             'network_connection',
#             'active_directory',
#             'ip_address',
#             'organizational_unit',
#             'sccm',
#             'jamf',
#             'scep',
#             'identity_finder',
#             'notes'
#         ]
    
#     def clean_computer_name(self):
#         computer_name = self.cleaned_data.get('computer_name')
#         if computer_name is None:
#             raise forms.ValidationError('This field cannot be left blank')
#         return computer_name

# class AssetSearchForm(forms.ModelForm):
#     class Meta:
#         model = Asset
#         fields = ['asset_tag',]