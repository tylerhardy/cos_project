# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cos', '0010_auto_20170731_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]