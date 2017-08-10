# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 17:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cos', '0007_auto_20170714_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_user', to=settings.AUTH_USER_MODEL),
        ),
    ]