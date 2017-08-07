from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import datetime

hardware_role_choice = (
    ('faculty_main', "Faculty Main"),
    ('faculty_secondary', "Faculty Secondary"),
    ('classroom_hardware', "Classroom"),
    ('instrument_hardware', "Instrument"),
    ('lab_research', "Research Lab"),
    ('lab_open', "Open Lab"),
    ('lab_closed', "Closed Lab"),
    ('department_travel', "Department Travel"),
    ('staff_main', "Staff Main"),
    ('staff_secondary', "Staff Secondary"),
    ('stock', "In Stock"),
    ('surplus', "Surplused"),
    ('other', "Other"),
)

condition_choices = (
    ('new', "New"),
    ('good', "Good"),
    ('used', "Used"),
    ('worn', "Worn out"),
    ('broken', "Broken"),
)

inventory_system_choices = (
    ('pc_lifecycle', "PC Lifecycle"),
    ('property_control', "Property Control"),
    ('old', "Old Inventory Tag"),
    ('None', 'No Tag')
)

org_code_choice = (
    ('25000',"25000 - Dean's Office"),
    ('25100','25100 - Botany'),
    ('25200','25200 - Chemistry'),
    ('25300','25300 - Geosciences'),
    ('25400','25400 - Mathematics'),
    ('25403','25403 - Developmental Math'),
    ('25500','25500 - Microbiology'),
    ('25600','25600 - Physics'),
    ('25601','25601 - Planetarium'),
    ('25700','25700 - Zoology'),
    ('25801','25801 - CSME'),
    ('None','No organization code'),
)

department_choice = (
    ('dean',"Dean's office"),
    ('bot','Botany'),
    ('chem','Chemistry'),
    ('geo','Geosciences'),
    ('math','Mathematics'),
    ('dev_math','Developmental Math'),
    ('micro','Microbiology'),
    ('phys','Physics'),
    ('planet_phys','Planetarium'),
    ('zoo','Zoology'),
    ('csme','Center of Science and Math Education'),
    ('other','Other or Unknown Department'),
    ('None','No department')
)

hardware_type_choice = (
    ('desktop', 'Desktop'),
    ('laptop', 'Laptop'),
    ('tablet', 'Tablet'),
    ('printer', 'Printer'),
    ('projector', 'Projector'),
    ('tv', 'TV or Monitor'),
    ('extron', 'Extron'),
    ('doc_cam', 'Document Camera'),
    ('camera', 'Camera'),
    ('other', 'Other'),
)

os_choice = (
    ('osx_10.5','Mac OS X Leopard'),
    ('osx_10.6','Mac OS X Snow Leopard'),
    ('osx_10.7','Mac OS X Lion'),
    ('osx_10.8','Mac OS X Mountain Lion'),
    ('osx_10.9','Mac OS X Macericks'),
    ('osx_10.10','Mac OS X Yosemite'),
    ('osx_10.11','Mac OS X El Capitan'),
    ('osx_10.12','Mac OS X Sierra'),
    ('osx_10.13','Mac OS X High Sierra'),
    ('win_xp_home','Windows XP Home'),
    ('win_xp_pro','Windows XP Pro'),
    ('win_vista_home','Windows Vista Home'),
    ('win_vista_pro','Windows Vista Pro'),
    ('win_vista_ent','Windows Vista Enterprise'),
    ('win_7_home','Windows 7 Home'),
    ('win_7_pro','Windows 7 Pro'),
    ('win_7_ent','Windows 7 Enterprise'),
    ('win_8','Windows 8'),
    ('win_8_pro','Windows 8 Pro'),
    ('win_8_ent','Windows 8 Enterprise'),
    ('win_8_1','Windows 8.1'),
    ('win_8_1_pro','Windows 8.1 Pro'),
    ('win_8_1_ent','Windows 8.1 Enterprise'),
    ('win_10_home','Windows 10 Home'),
    ('win_10_pro','Windows 10 Pro'),
    ('win_10_ent','Windows 10 Enterprise'),
    ('win_10_ent_ltsb','Windows 10 Enterprise LTSB'),
    ('linux', 'Linux Distro'),
    ('other', 'Other OS'),
    ('none','No OS installed')
)

os_arch_choice = (
    ('x86','32-Bit'),
    ('x64','64-Bit'),
    ('other','Other'),
    ('none','No OS installed')
)

connection_choice = (
    ('WD', 'Wired'),
    ('WL', 'Wireless'),
    ('none', 'No Network Connection')
)
# ['asset_tag', 'hardware_name', 'hardware_role', 'hardware_condition', 'inventory_system', 'inventory_system_current', 'user', 'curator', 'department', 'org_code', 'location', 'vendor', 'vendor_serial_number', 'purchase_order', 'purchase_date', 'purchase_cost', 'funded_by', 'hardware_type', 'hardware_make', 'hardware_model', 'hardware_serial_number', 'network_connection', 'ip_address', 'mac_wired', 'mac_wireless', 'processor', 'harddrive', 'ram', 'graphics', 'os', 'os_arch', 'active_directory', 'organizational_unit', 'sccm', 'jamf', 'scep', 'identity_finder', 'notes']

# Create your models here.
class Asset(models.Model):
    """The Hardware info of the asset"""
    asset_tag = models.CharField(max_length=200, unique=True)
    hardware_name = models.CharField(max_length=200, blank=True)
    hardware_role = models.CharField(max_length=200, blank=True, choices=hardware_role_choice)
    hardware_condition = models.CharField("Condition", max_length=200, blank=True, choices=condition_choices)
    inventory_system = models.CharField("Inventory system", max_length=200, blank=True, choices=inventory_system_choices)
    inventory_system_current = models.BooleanField("Inventory system Up-To-Date", default=False)
    user = models.CharField("Primary user", max_length=200, blank=True)
    curator = models.CharField("Curator", max_length=200, blank=True)
    department = models.CharField("Department", max_length=200, blank=True, choices=department_choice)
    org_code = models.CharField("Department orginational code", max_length=200, blank=True, choices=org_code_choice)
    location = models.CharField("Location", max_length=200, blank=True)
    vendor = models.CharField("Vendor",max_length=200, blank=True)
    vendor_serial_number = models.CharField("Vendor serial number", max_length=200, unique=True, blank=True, null=True)
    purchase_order = models.CharField("PO", max_length=200, blank=True)
    purchase_date = models.DateTimeField("Date of purchase", blank=True, null=True)
    purchase_cost = models.CharField("Cost", max_length=200, blank=True)
    funded_by = models.CharField("Hardware source of funds", max_length=200, blank=True)
    hardware_type = models.CharField(max_length=200, choices=hardware_type_choice)
    hardware_make = models.CharField(max_length=200, blank=True)
    hardware_model = models.CharField(max_length=200, blank=True)
    hardware_serial_number = models.CharField(max_length=200, unique=True, blank=True, null=True)
    network_connection = models.CharField("Network connection", max_length=30, choices=connection_choice, blank=True)
    ip_address = models.GenericIPAddressField(protocol='IPv4', blank=True, null=True)
    mac_wired = models.CharField(max_length=200, unique=True, blank=True, null=True)
    mac_wireless = models.CharField(max_length=200, unique=True, blank=True, null=True)
    processor = models.CharField(max_length=200, blank=True)
    harddrive = models.CharField(max_length=200, blank=True)
    ram = models.CharField(max_length=200, blank=True)
    graphics = models.CharField(max_length=200, blank=True)
    os = models.CharField("Installed OS", max_length=200, choices=os_choice, blank=True)
    os_arch = models.CharField("OS architecture", max_length=30, choices=os_arch_choice, blank=True)
    active_directory = models.BooleanField("Managed on the Domain", default=False)
    organizational_unit = models.CharField("OU location", max_length=200, blank=True)
    sccm = models.BooleanField("Listed in SCCM", default=False)
    jamf = models.BooleanField("Listed in JAMF", default=False)
    scep = models.BooleanField("SCEP installed and up-to-date", default=False)
    identity_finder = models.BooleanField("Identity Finder installed", default=False)
    notes = models.TextField(blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, related_name='added_user', blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey(User, related_name='modified_user', blank=True, null=True)
    deleted = models.BooleanField(default=False)
    deleted_date = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(User, related_name='deleted_user', blank=True, null=True)
    audited_date = models.DateTimeField(blank=True, null=True)
    audited_by = models.ForeignKey(User, related_name='audited_user', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('asset-detail', args=[str(self.id)])

    def __str__(self):
        """Return a string representation of the model."""
        return self.asset_tag

    def save(self, *args, **kwargs):
        if self.pk is None:
            # Create Object
            self.added_date = datetime.datetime.now()
        else:
            # Modify Object
            self.modified_date = datetime.datetime.now()
        super(Asset, self).save(*args, **kwargs)