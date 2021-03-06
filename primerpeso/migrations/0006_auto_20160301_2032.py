# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-01 20:32
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerpeso', '0005_auto_20160301_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opportunitysearch',
            name='benefit_types',
        ),
        migrations.RemoveField(
            model_name='opportunitysearch',
            name='demographics',
        ),
        migrations.AlterField(
            model_name='opportunitysearch',
            name='age',
            field=models.IntegerField(verbose_name='What is the age of the owners?'),
        ),
        migrations.AlterField(
            model_name='opportunitysearch',
            name='annual_revenue',
            field=models.IntegerField(verbose_name='What is your annual revenue?'),
        ),
        migrations.AlterField(
            model_name='opportunitysearch',
            name='employees',
            field=models.IntegerField(verbose_name='How many full time employees do you have?'),
        ),
        migrations.AlterField(
            model_name='opportunitysearch',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('both', 'Both'), ('other', 'Other')], max_length=6, verbose_name='What owners genders?'),
        ),
        migrations.AlterField(
            model_name='opportunitysearch',
            name='investing_own_money',
            field=models.BooleanField(verbose_name='Will you invest personal money?'),
        ),
        migrations.AlterField(
            model_name='opportunitysearch',
            name='purpose',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('anything', 'Cualquiera'), ('open_location', 'Abrir un Nuevo Local'), ('open_franchise', 'Abrir una Franquicia'), ('train_employees', 'Adiestrar Empleados'), ('working_capital', 'Capital de trabajo'), ('buy_equipment', 'Comprar Equipo'), ('buy_commercial_property', 'Comprar una propiedad comercial'), ('hire_employees', 'Contratar Empleados  / Pasantes'), ('start_business', 'Crear un Negocio'), ('export', 'Exportar'), ('export_products', 'Exportar productos'), ('export_services', 'Exportar servicios'), ('improve_commercial_property', 'Mejorar una propiedad comercial'), ('cinematographic_production', 'Producción Cinematográfica'), ('keep_employees', 'Retener empleados'), ('relocate_business', 'Reubicar un Negocio'), ('other', 'Otro (Por favor especifíca el propósito)')], max_length=255), default=list, size=None, verbose_name='How would you use the incentive?'),
        ),
        migrations.AlterField(
            model_name='opportunitysearch',
            name='years_in_business',
            field=models.IntegerField(verbose_name='How many years have you been in business?'),
        ),
    ]
