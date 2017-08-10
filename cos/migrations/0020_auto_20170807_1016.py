# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cos', '0019_auto_20170802_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='equipment_condition',
            new_name='hardware_condition',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='computer_name',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='equipment_role',
        ),
        migrations.AddField(
            model_name='asset',
            name='hardware_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Hardware Name*'),
        ),
        migrations.AddField(
            model_name='asset',
            name='hardware_role',
            field=models.CharField(blank=True, choices=[('faculty_main', 'Faculty Main Hardware'), ('faculty_secondary', 'Faculty Secondary Hardware'), ('classroom_hardware', 'Classroom Hardware'), ('instrument_hardware', 'Instrument Hardware'), ('lab_research', 'Research Lab Hardware'), ('lab_open', 'Open Lab Hardware'), ('lab_closed', 'Closed Lab Hardware'), ('department_travel', 'Department Travel Hardware'), ('staff_main', 'Staff Main Hardware'), ('staff_secondary', 'Staff Secondary Hardware'), ('stock', 'In Stock Hardware'), ('surplus', 'Surplused Hardware'), ('other', 'Other Hardware')], max_length=200, verbose_name='Hardware primary role'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='active_directory',
            field=models.BooleanField(default=False, verbose_name='Hardware managed on the Domain'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_tag',
            field=models.CharField(max_length=200, unique=True, verbose_name='Asset Tag*'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='curator',
            field=models.CharField(blank=True, max_length=200, verbose_name='Hardware curator'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='department',
            field=models.CharField(blank=True, choices=[('dean', "Dean's office"), ('bot', 'Botany'), ('chem', 'Chemistry'), ('geo', 'Geosciences'), ('math', 'Mathematics'), ('dev_math', 'Developmental Math'), ('micro', 'Microbiology'), ('phys', 'Physics'), ('planet_phys', 'Planetarium'), ('zoo', 'Zoology'), ('csme', 'Center of Science and Math Education'), ('other', 'Other or Unknown Department'), ('None', 'No department')], max_length=200, verbose_name='Hardware department'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='funded_by',
            field=models.CharField(blank=True, max_length=200, verbose_name='Hardware source of funds'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='hardware_type',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='asset',
            name='jamf',
            field=models.BooleanField(default=False, verbose_name='Listed in JAMF'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='location',
            field=models.CharField(blank=True, max_length=200, verbose_name='Hardware location'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='network_connection',
            field=models.CharField(blank=True, choices=[('WD', 'Wired'), ('WL', 'Wireless'), ('none', 'No Network Connection')], max_length=30, verbose_name='Hardware network connection'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='org_code',
            field=models.CharField(blank=True, choices=[('25000', "25000 - Dean's Office"), ('25100', '25100 - Botany'), ('25200', '25200 - Chemistry'), ('25300', '25300 - Geosciences'), ('25400', '25400 - Mathematics'), ('25403', '25403 - Developmental Math'), ('25500', '25500 - Microbiology'), ('25600', '25600 - Physics'), ('25601', '25601 - Planetarium'), ('25700', '25700 - Zoology'), ('25801', '25801 - CSME'), ('None', 'No organization code')], max_length=200, verbose_name='Department orginational code'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='organizational_unit',
            field=models.CharField(blank=True, max_length=200, verbose_name='Hardware OU location'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='os_arch',
            field=models.CharField(blank=True, choices=[('x86', '32-Bit'), ('x64', '64-Bit'), ('other', 'Other'), ('none', 'No OS installed')], max_length=30, verbose_name='OS architecture'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='purchase_cost',
            field=models.CharField(blank=True, max_length=200, verbose_name='Hardware cost'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='sccm',
            field=models.BooleanField(default=False, verbose_name='Listed in SCCM'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='scep',
            field=models.BooleanField(default=False, verbose_name='SCEP installed and up-to-date'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='vendor',
            field=models.CharField(blank=True, max_length=200, verbose_name='Hardware vendor'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='vendor_serial_number',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Vendor serial number'),
        ),
    ]