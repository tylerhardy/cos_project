# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 22:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_tag', models.CharField(max_length=200, unique=True)),
                ('hardware_name', models.CharField(blank=True, max_length=200)),
                ('hardware_role', models.CharField(blank=True, choices=[('faculty_main', 'Faculty Main'), ('faculty_secondary', 'Faculty Secondary'), ('classroom_hardware', 'Classroom'), ('instrument_hardware', 'Instrument'), ('lab_research', 'Research Lab'), ('lab_open', 'Open Lab'), ('lab_closed', 'Closed Lab'), ('department_travel', 'Department Travel'), ('staff_main', 'Staff Main'), ('staff_secondary', 'Staff Secondary'), ('stock', 'In Stock'), ('surplus', 'Surplused'), ('other', 'Other')], max_length=200)),
                ('hardware_condition', models.CharField(blank=True, choices=[('good', 'Good'), ('old', 'Old'), ('broken', 'Broken')], max_length=200, verbose_name='Condition')),
                ('inventory_system', models.CharField(blank=True, choices=[('pc_lifecycle', 'PC Lifecycle'), ('property_control', 'Property Control'), ('old', 'Old Inventory Tag'), ('None', 'No Tag')], max_length=200, verbose_name='Inventory system')),
                ('user', models.CharField(blank=True, max_length=200, verbose_name='Primary user')),
                ('curator', models.CharField(blank=True, max_length=200, verbose_name='Curator')),
                ('department', models.CharField(blank=True, choices=[('dean', "Dean's office"), ('bot', 'Botany'), ('chem', 'Chemistry'), ('geo', 'Geosciences'), ('math', 'Mathematics'), ('dev_math', 'Developmental Math'), ('micro', 'Microbiology'), ('phys', 'Physics'), ('planet_phys', 'Planetarium'), ('zoo', 'Zoology'), ('csme', 'Center of Science and Math Education'), ('other', 'Other or Unknown Department'), ('None', 'No department')], max_length=200, verbose_name='Department')),
                ('org_code', models.CharField(blank=True, choices=[('25000', "25000 - Dean's Office"), ('25100', '25100 - Botany'), ('25200', '25200 - Chemistry'), ('25300', '25300 - Geosciences'), ('25400', '25400 - Mathematics'), ('25403', '25403 - Developmental Math'), ('25500', '25500 - Microbiology'), ('25600', '25600 - Physics'), ('25601', '25601 - Planetarium'), ('25700', '25700 - Zoology'), ('25801', '25801 - CSME'), ('None', 'No organization code')], max_length=200, verbose_name='Department orginational code')),
                ('location', models.CharField(blank=True, max_length=200, verbose_name='Location')),
                ('vendor', models.CharField(blank=True, max_length=200, verbose_name='Vendor')),
                ('vendor_serial_number', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Vendor serial number')),
                ('requisition_number', models.CharField(blank=True, max_length=200, verbose_name='Requisition number')),
                ('purchase_order', models.CharField(blank=True, max_length=200, verbose_name='PO')),
                ('purchase_date', models.DateTimeField(blank=True, null=True, verbose_name='Date of purchase')),
                ('purchase_cost', models.CharField(blank=True, max_length=200, verbose_name='Cost')),
                ('eligible_upgrade', models.IntegerField(blank=True, choices=[(0, 'None'), (1, '1 years'), (2, '2 years'), (3, '3 years'), (4, '4 years'), (5, '5 years'), (6, '6 years'), (7, '7 years'), (8, '8 years'), (9, '9 years'), (10, '10 years')], default=0, null=True, verbose_name='Upgrade eligibility')),
                ('eligible_upgrade_date', models.DateTimeField(blank=True, null=True, verbose_name='Upgrade eligibility date')),
                ('funded_by', models.CharField(blank=True, max_length=200, verbose_name='Hardware source of funds')),
                ('hardware_type', models.CharField(blank=True, choices=[('desktop', 'Desktop'), ('laptop', 'Laptop'), ('tablet', 'Tablet'), ('printer', 'Printer'), ('projector', 'Projector'), ('tv', 'TV or Monitor'), ('extron', 'Extron'), ('doc_cam', 'Document Camera'), ('camera', 'Camera'), ('other', 'Other')], max_length=200)),
                ('hardware_make', models.CharField(blank=True, max_length=200)),
                ('hardware_model', models.CharField(blank=True, max_length=200)),
                ('hardware_serial_number', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('network_connection', models.CharField(blank=True, choices=[('WD', 'Wired'), ('WL', 'Wireless'), ('none', 'No Network Connection')], max_length=30, verbose_name='Network connection')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')),
                ('mac_wired', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('mac_wireless', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('processor', models.CharField(blank=True, max_length=200)),
                ('harddrive', models.CharField(blank=True, max_length=200)),
                ('ram', models.CharField(blank=True, max_length=200)),
                ('graphics', models.CharField(blank=True, max_length=200)),
                ('os', models.CharField(blank=True, choices=[('osx_10.5', 'Mac OS X Leopard'), ('osx_10.6', 'Mac OS X Snow Leopard'), ('osx_10.7', 'Mac OS X Lion'), ('osx_10.8', 'Mac OS X Mountain Lion'), ('osx_10.9', 'Mac OS X Macericks'), ('osx_10.10', 'Mac OS X Yosemite'), ('osx_10.11', 'Mac OS X El Capitan'), ('osx_10.12', 'Mac OS X Sierra'), ('osx_10.13', 'Mac OS X High Sierra'), ('win_xp_home', 'Windows XP Home'), ('win_xp_pro', 'Windows XP Pro'), ('win_vista_home', 'Windows Vista Home'), ('win_vista_pro', 'Windows Vista Pro'), ('win_vista_ent', 'Windows Vista Enterprise'), ('win_7_home', 'Windows 7 Home'), ('win_7_pro', 'Windows 7 Pro'), ('win_7_ent', 'Windows 7 Enterprise'), ('win_8', 'Windows 8'), ('win_8_pro', 'Windows 8 Pro'), ('win_8_ent', 'Windows 8 Enterprise'), ('win_8_1', 'Windows 8.1'), ('win_8_1_pro', 'Windows 8.1 Pro'), ('win_8_1_ent', 'Windows 8.1 Enterprise'), ('win_10_home', 'Windows 10 Home'), ('win_10_pro', 'Windows 10 Pro'), ('win_10_ent', 'Windows 10 Enterprise'), ('win_10_ent_ltsb', 'Windows 10 Enterprise LTSB'), ('linux', 'Linux Distro'), ('other', 'Other OS'), ('none', 'No OS installed')], max_length=200, verbose_name='Installed OS')),
                ('os_arch', models.CharField(blank=True, choices=[('x86', '32-Bit'), ('x64', '64-Bit'), ('other', 'Other'), ('none', 'No OS installed')], max_length=30, verbose_name='OS architecture')),
                ('active_directory', models.BooleanField(default=False, verbose_name='Managed on the Domain')),
                ('organizational_unit', models.CharField(blank=True, max_length=200, verbose_name='OU location')),
                ('sccm', models.BooleanField(default=False, verbose_name='Listed in SCCM')),
                ('jamf', models.BooleanField(default=False, verbose_name='Listed in JAMF')),
                ('scep', models.BooleanField(default=False, verbose_name='SCEP installed and up-to-date')),
                ('identity_finder', models.BooleanField(default=False, verbose_name='Identity Finder installed')),
                ('notes', models.TextField(blank=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('audited_date', models.DateTimeField(blank=True, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_user', to=settings.AUTH_USER_MODEL)),
                ('audited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audited_user', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deleted_user', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalAsset',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('asset_tag', models.CharField(db_index=True, max_length=200)),
                ('hardware_name', models.CharField(blank=True, max_length=200)),
                ('hardware_role', models.CharField(blank=True, choices=[('faculty_main', 'Faculty Main'), ('faculty_secondary', 'Faculty Secondary'), ('classroom_hardware', 'Classroom'), ('instrument_hardware', 'Instrument'), ('lab_research', 'Research Lab'), ('lab_open', 'Open Lab'), ('lab_closed', 'Closed Lab'), ('department_travel', 'Department Travel'), ('staff_main', 'Staff Main'), ('staff_secondary', 'Staff Secondary'), ('stock', 'In Stock'), ('surplus', 'Surplused'), ('other', 'Other')], max_length=200)),
                ('hardware_condition', models.CharField(blank=True, choices=[('good', 'Good'), ('old', 'Old'), ('broken', 'Broken')], max_length=200, verbose_name='Condition')),
                ('inventory_system', models.CharField(blank=True, choices=[('pc_lifecycle', 'PC Lifecycle'), ('property_control', 'Property Control'), ('old', 'Old Inventory Tag'), ('None', 'No Tag')], max_length=200, verbose_name='Inventory system')),
                ('user', models.CharField(blank=True, max_length=200, verbose_name='Primary user')),
                ('curator', models.CharField(blank=True, max_length=200, verbose_name='Curator')),
                ('department', models.CharField(blank=True, choices=[('dean', "Dean's office"), ('bot', 'Botany'), ('chem', 'Chemistry'), ('geo', 'Geosciences'), ('math', 'Mathematics'), ('dev_math', 'Developmental Math'), ('micro', 'Microbiology'), ('phys', 'Physics'), ('planet_phys', 'Planetarium'), ('zoo', 'Zoology'), ('csme', 'Center of Science and Math Education'), ('other', 'Other or Unknown Department'), ('None', 'No department')], max_length=200, verbose_name='Department')),
                ('org_code', models.CharField(blank=True, choices=[('25000', "25000 - Dean's Office"), ('25100', '25100 - Botany'), ('25200', '25200 - Chemistry'), ('25300', '25300 - Geosciences'), ('25400', '25400 - Mathematics'), ('25403', '25403 - Developmental Math'), ('25500', '25500 - Microbiology'), ('25600', '25600 - Physics'), ('25601', '25601 - Planetarium'), ('25700', '25700 - Zoology'), ('25801', '25801 - CSME'), ('None', 'No organization code')], max_length=200, verbose_name='Department orginational code')),
                ('location', models.CharField(blank=True, max_length=200, verbose_name='Location')),
                ('vendor', models.CharField(blank=True, max_length=200, verbose_name='Vendor')),
                ('vendor_serial_number', models.CharField(blank=True, db_index=True, max_length=200, null=True, verbose_name='Vendor serial number')),
                ('requisition_number', models.CharField(blank=True, max_length=200, verbose_name='Requisition number')),
                ('purchase_order', models.CharField(blank=True, max_length=200, verbose_name='PO')),
                ('purchase_date', models.DateTimeField(blank=True, null=True, verbose_name='Date of purchase')),
                ('purchase_cost', models.CharField(blank=True, max_length=200, verbose_name='Cost')),
                ('eligible_upgrade', models.IntegerField(blank=True, choices=[(0, 'None'), (1, '1 years'), (2, '2 years'), (3, '3 years'), (4, '4 years'), (5, '5 years'), (6, '6 years'), (7, '7 years'), (8, '8 years'), (9, '9 years'), (10, '10 years')], default=0, null=True, verbose_name='Upgrade eligibility')),
                ('eligible_upgrade_date', models.DateTimeField(blank=True, null=True, verbose_name='Upgrade eligibility date')),
                ('funded_by', models.CharField(blank=True, max_length=200, verbose_name='Hardware source of funds')),
                ('hardware_type', models.CharField(blank=True, choices=[('desktop', 'Desktop'), ('laptop', 'Laptop'), ('tablet', 'Tablet'), ('printer', 'Printer'), ('projector', 'Projector'), ('tv', 'TV or Monitor'), ('extron', 'Extron'), ('doc_cam', 'Document Camera'), ('camera', 'Camera'), ('other', 'Other')], max_length=200)),
                ('hardware_make', models.CharField(blank=True, max_length=200)),
                ('hardware_model', models.CharField(blank=True, max_length=200)),
                ('hardware_serial_number', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('network_connection', models.CharField(blank=True, choices=[('WD', 'Wired'), ('WL', 'Wireless'), ('none', 'No Network Connection')], max_length=30, verbose_name='Network connection')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, protocol='IPv4')),
                ('mac_wired', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('mac_wireless', models.CharField(blank=True, db_index=True, max_length=200, null=True)),
                ('processor', models.CharField(blank=True, max_length=200)),
                ('harddrive', models.CharField(blank=True, max_length=200)),
                ('ram', models.CharField(blank=True, max_length=200)),
                ('graphics', models.CharField(blank=True, max_length=200)),
                ('os', models.CharField(blank=True, choices=[('osx_10.5', 'Mac OS X Leopard'), ('osx_10.6', 'Mac OS X Snow Leopard'), ('osx_10.7', 'Mac OS X Lion'), ('osx_10.8', 'Mac OS X Mountain Lion'), ('osx_10.9', 'Mac OS X Macericks'), ('osx_10.10', 'Mac OS X Yosemite'), ('osx_10.11', 'Mac OS X El Capitan'), ('osx_10.12', 'Mac OS X Sierra'), ('osx_10.13', 'Mac OS X High Sierra'), ('win_xp_home', 'Windows XP Home'), ('win_xp_pro', 'Windows XP Pro'), ('win_vista_home', 'Windows Vista Home'), ('win_vista_pro', 'Windows Vista Pro'), ('win_vista_ent', 'Windows Vista Enterprise'), ('win_7_home', 'Windows 7 Home'), ('win_7_pro', 'Windows 7 Pro'), ('win_7_ent', 'Windows 7 Enterprise'), ('win_8', 'Windows 8'), ('win_8_pro', 'Windows 8 Pro'), ('win_8_ent', 'Windows 8 Enterprise'), ('win_8_1', 'Windows 8.1'), ('win_8_1_pro', 'Windows 8.1 Pro'), ('win_8_1_ent', 'Windows 8.1 Enterprise'), ('win_10_home', 'Windows 10 Home'), ('win_10_pro', 'Windows 10 Pro'), ('win_10_ent', 'Windows 10 Enterprise'), ('win_10_ent_ltsb', 'Windows 10 Enterprise LTSB'), ('linux', 'Linux Distro'), ('other', 'Other OS'), ('none', 'No OS installed')], max_length=200, verbose_name='Installed OS')),
                ('os_arch', models.CharField(blank=True, choices=[('x86', '32-Bit'), ('x64', '64-Bit'), ('other', 'Other'), ('none', 'No OS installed')], max_length=30, verbose_name='OS architecture')),
                ('active_directory', models.BooleanField(default=False, verbose_name='Managed on the Domain')),
                ('organizational_unit', models.CharField(blank=True, max_length=200, verbose_name='OU location')),
                ('sccm', models.BooleanField(default=False, verbose_name='Listed in SCCM')),
                ('jamf', models.BooleanField(default=False, verbose_name='Listed in JAMF')),
                ('scep', models.BooleanField(default=False, verbose_name='SCEP installed and up-to-date')),
                ('identity_finder', models.BooleanField(default=False, verbose_name='Identity Finder installed')),
                ('notes', models.TextField(blank=True)),
                ('added_date', models.DateTimeField(blank=True, editable=False)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('audited_date', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('added_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('audited_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical asset',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
    ]
