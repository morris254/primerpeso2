# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-15 17:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primerpeso', '0010_auto_20160307_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunitysearch',
            name='age',
        ),
    ]
