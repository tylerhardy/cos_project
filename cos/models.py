from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Asset(models.Model):
    """The Hardware info of the asset"""
    asset_tag = models.CharField(max_length=200)
    pc_lifecycle = models.BooleanField()
    property_control = models.BooleanField()
    owner = models.CharField(max_length=200)
    curator = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    org_code = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    vendor = models.CharField(max_length=200)
    vendor_serial_number = models.CharField(max_length=200)
    purchase_order = models.CharField(max_length=200)
    purchase_date = models.DateTimeField()
    purchase_cost = models.CharField(max_length=200)
    funded_by = models.CharField(max_length=200)
    hardware_type = models.CharField(max_length=200)
    hardware_make = models.CharField(max_length=200)
    hardware_model = models.CharField(max_length=200)
    hardware_serial_number = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=200)
    mac_wired = models.CharField(max_length=200)
    mac_wireless = models.CharField(max_length=200)
    processor = models.CharField(max_length=200)
    harddrive = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    graphics = models.CharField(max_length=200)
    notes = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User)
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User)
    deleted = models.BooleanField()
    deleted_date = models.DateTimeField(auto_now=True)
    deleted_by = models.ForeignKey(User)
    audited_date = models.DateTimeField(auto_now=True)
    audited_by = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model."""
        return self.asset_tag

class ComputerObject(models.Model):
    """The Computer Object info of the asset"""
    asset = models.ForeignKey(Asset)
    computer_name = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    connection_choice = (
        ('WD', 'Wired'),
        ('WL', 'Wireless'),
    )
    network_connection = models.CharField(max_length=30, choices=connection_choice)
    active_directory = models.BooleanField()
    organizational_unit = models.CharField(max_length=200)
    sccm = models.BooleanField()
    jamf = models.BooleanField()
    scep = models.BooleanField()
    identity_finder = models.BooleanField()
    notes = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User)
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User)
    deleted = models.BooleanField()
    deleted_date = models.DateTimeField(auto_now=True)
    deleted_by = models.ForeignKey(User)
    audited_date = models.DateTimeField(auto_now=True)
    audited_by = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model."""
        return self.computer_name