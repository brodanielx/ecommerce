# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-12 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20180312_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingprofile',
            name='customer_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
