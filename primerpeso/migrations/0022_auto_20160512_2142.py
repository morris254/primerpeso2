# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-12 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerpeso', '0021_auto_20160330_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.CharField(max_length=255, verbose_name='Legal Business Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='incorporated',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False, verbose_name='Are You Incorporated?'),
        ),
        migrations.AlterField(
            model_name='opportunitysearch',
            name='annual_revenue',
            field=models.IntegerField(verbose_name='What was the gross revenue for your last fiscal calendar year?'),
        ),
    ]
