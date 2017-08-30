from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from django.utils import timezone
from simple_history.models import HistoricalRecords

# Hardware role
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

# Condition of hardware
condition_choices = (
    ('good', "Good"),
    ('old', "Old"),
    ('broken', "Broken"),
)

# Inventory system that hardware belongs to
inventory_system_choices = (
    ('pc_lifecycle', "PC Lifecycle"),
    ('property_control', "Property Control"),
    ('old', "Old Inventory Tag"),
    ('None', 'No Tag')
)

# Department organization codes
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

# College of Science Departments
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

# Hardware Type
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

# Operating Systems
os_choice = (
    ('osx_10.5','Mac OS X Leopard (10.5)'),
    ('osx_10.6','Mac OS X Snow Leopard (10.6)'),
    ('osx_10.7','Mac OS X Lion (10.7)'),
    ('osx_10.8','Mac OS X Mountain Lion (10.8)'),
    ('osx_10.9','Mac OS X Macericks (10.9)'),
    ('osx_10.10','Mac OS X Yosemite (10.10)'),
    ('osx_10.11','Mac OS X El Capitan (10.11)'),
    ('osx_10.12','Mac OS X Sierra (10.12)'),
    ('osx_10.13','Mac OS X High Sierra (10.13)'),
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

# OS Architecture
os_arch_choice = (
    ('x86','32-Bit'),
    ('x64','64-Bit'),
    ('other','Other'),
    ('none','No OS installed')
)

# Eligibilty Choices
eligible_upgrade_choice = (
    (0, 'None'),
    (1, '1 years'),
    (2, '2 years'),
    (3, '3 years'),
    (4, '4 years'),
    (5, '5 years'),
    (6, '6 years'),
    (7, '7 years'),
    (8, '8 years'),
    (9, '9 years'),
    (10, '10 years')
)

# Hardware network connection
connection_choice = (
    ('WD', 'Wired'),
    ('WL', 'Wireless'),
    ('none', 'No Network Connection')
)

# Create your models here.
class Asset(models.Model):
    """
    Asset model of the hardware in the inventory system
    """
    asset_tag = models.CharField(max_length=200, unique=True)
    hardware_name = models.CharField(max_length=200, blank=True)
    hardware_role = models.CharField(max_length=200, blank=True, choices=hardware_role_choice)
    hardware_condition = models.CharField("Condition", max_length=200, blank=True, choices=condition_choices)
    inventory_system = models.CharField("Inventory system", max_length=200, blank=True, choices=inventory_system_choices)
    user = models.CharField("Primary user", max_length=200, blank=True)
    curator = models.CharField("Curator", max_length=200, blank=True)
    department = models.CharField("Department", max_length=200, blank=True, choices=department_choice)
    org_code = models.CharField("Department orginational code", max_length=200, blank=True, choices=org_code_choice)
    location = models.CharField("Location", max_length=200, blank=True)
    vendor = models.CharField("Vendor",max_length=200, blank=True)
    vendor_serial_number = models.CharField("Vendor serial number", max_length=200, unique=True, blank=True, null=True)
    requisition_number = models.CharField("Requisition number", max_length=200, blank=True)
    purchase_order = models.CharField("PO", max_length=200, blank=True)
    purchase_date = models.DateTimeField("Date of purchase", blank=True, null=True)
    purchase_cost = models.CharField("Cost", max_length=200, blank=True)
    eligible_upgrade = models.IntegerField("Upgrade eligibility", default=0, choices=eligible_upgrade_choice, blank=True, null=True)
    eligible_upgrade_date = models.DateTimeField("Upgrade eligibility date", blank=True, null=True)
    funded_by = models.CharField("Hardware source of funds", max_length=200, blank=True)
    hardware_type = models.CharField(max_length=200, choices=hardware_type_choice, blank=True)
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
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse('asset_detail', args=[str(self.id)])

    def __str__(self):
        """
        Return a string representation of the model.
        """
        return self.asset_tag

    def save(self, *args, **kwargs):
        if self.purchase_date:
            if self.eligible_upgrade:
                self.eligible_upgrade_date = self.purchase_date + datetime.timedelta(days=((365 * self.eligible_upgrade)+1))
            else:
                self.eligible_upgrade_date = None
        else:
            self.eligible_upgrade_date = None
        super(Asset, self).save(*args, **kwargs)

    @property
    def is_eligible_upgrade(self):
        d_now = timezone.make_aware(datetime.datetime.today())
        d_1yr = timezone.make_aware(datetime.datetime.today()) + datetime.timedelta(days=365)
        d_4yr = timezone.make_aware(datetime.datetime.today()) + datetime.timedelta(days=1460)
        d_5yr = timezone.make_aware(datetime.datetime.today()) + datetime.timedelta(days=1825)
        if self.eligible_upgrade_date >= d_1yr:
            return 'not_eligible'
        elif (self.eligible_upgrade_date < d_1yr) and (self.eligible_upgrade_date > d_now):
            return 'almost_eligible'
        elif self.eligible_upgrade_date < d_now:
            return 'is_eligible'
        else:
            return 'error'

    # @property
    # def is_past_due(self):
    #     d_180 = timezone.make_aware(datetime.datetime.today()) - datetime.timedelta(days=180)
    #     d_365 = timezone.make_aware(datetime.datetime.today()) - datetime.timedelta(days=365)
    #     if self.audited_date is None:
    #         # return print("no_audit_performed")
    #         return 'no_audit_performed'
    #     if self.audited_date > d_180:
    #         # return print("audit_good")
    #         return 'audit_good'
    #     elif (self.audited_date < d_180) and (self.audited_date > d_365):
    #         # return print("audit_old")
    #         return 'audit_old'
    #     elif self.audited_date < d_365:
    #         # return print("need_audit")
    #         return 'need_audit'
    #     else:
    #         # return print("missing_info")
    #         return 'missing_info'

    @property
    def is_past_due(self):
        d_180 = timezone.make_aware(datetime.datetime.today()) - datetime.timedelta(days=180)
        d_365 = timezone.make_aware(datetime.datetime.today()) - datetime.timedelta(days=365)
        if self.audited_date is None:
            return 'no_audit_performed'
        elif self.audited_date > d_180:
            return 'audit_good'
        elif (self.audited_date < d_180) and (self.audited_date > d_365):
            return 'audit_old'
        elif self.audited_date < d_365:
            return 'need_audit'
        else:
            return 'error'