# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-03 03:16
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('mission', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('fax', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.TextField(blank=True)),
                ('municipality', models.CharField(blank=True, max_length=255)),
                ('state', localflavor.us.models.USStateField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
                ('postal_code', localflavor.us.models.USPostalCodeField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FM', 'Federated States of Micronesia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MH', 'Marshall Islands'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PW', 'Palau'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
                ('web', models.URLField(blank=True, max_length=255)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Agencies',
                'verbose_name': 'Agency',
            },
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('any', 'Any'), ('other', 'Other')], max_length=6)),
                ('application_cost', models.IntegerField()),
                ('application_deadline', models.DateField()),
                ('benefit_description', models.TextField()),
                ('agency_contact_name', models.CharField(max_length=255)),
                ('agency_contact_phone', models.CharField(max_length=255)),
                ('agency_contact_email', models.EmailField(max_length=254)),
                ('minimum_years_in_business', models.IntegerField()),
                ('additional_information', models.TextField()),
                ('investing_own_money', models.BooleanField()),
                ('money_invested', models.CharField(max_length=255)),
                ('age_min', models.IntegerField()),
                ('age_max', models.IntegerField(blank=True, null=True)),
                ('employees_min', models.IntegerField()),
                ('employees_max', models.IntegerField(blank=True, null=True)),
                ('annual_revenue_min', models.IntegerField()),
                ('annual_revenue_max', models.IntegerField(blank=True, null=True)),
                ('average_application_time', models.CharField(blank=True, max_length=255)),
                ('locations', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('anywhere_in_pr', 'Cualquier municipio'), ('adjuntas', 'Adjuntas'), ('aguada', 'Aguada'), ('aguadilla', 'Aguadilla'), ('aguas_buenas', 'Aguas Buenas'), ('aibonito', 'Aibonito'), ('anasco', 'Añasco'), ('arecibo', 'Arecibo'), ('arroyo', 'Arroyo'), ('barceloneta', 'Barceloneta'), ('barranquitas', 'Barranquitas'), ('bayamon', 'Bayamón'), ('cabo_rojo', 'Cabo Rojo'), ('caguas', 'Caguas'), ('camuy', 'Camuy'), ('canovanas', 'Canóvanas'), ('carolina', 'Carolina'), ('catano', 'Cataño'), ('cayey', 'Cayey'), ('ceiba', 'Ceiba'), ('ciales', 'Ciales'), ('cidra', 'Cidra'), ('coamo', 'Coamo'), ('comerio', 'Comerio'), ('corozal', 'Corozal'), ('culebra', 'Culebra'), ('dorado', 'Dorado'), ('fajardo', 'Fajardo'), ('florida', 'Florida'), ('guanica', 'Guánica'), ('guayama', 'Guayama'), ('guayanilla', 'Guayanilla'), ('guaynabo', 'Guaynabo'), ('gurabo', 'Gurabo'), ('hatillo', 'Hatillo'), ('hormigueros', 'Hormigueros'), ('humacao', 'Humacao'), ('isabela', 'Isabela'), ('jayuya', 'Jayuya'), ('juana_diaz', 'Juana Diaz'), ('juncos', 'Juncos'), ('lajas', 'Lajas'), ('lares', 'Lares'), ('las_marias', 'Las Marías'), ('las_piedras', 'Las Piedras'), ('loiza', 'Loíza'), ('luquillo', 'Luquillo'), ('manati', 'Manatí'), ('maricao', 'Maricao'), ('maunabo', 'Maunabo'), ('mayaguez', 'Mayagüez'), ('moca', 'Moca'), ('morovis', 'Morovis'), ('naguabo', 'Naguabo'), ('naranjito', 'Naranjito'), ('orocovis', 'Orocovis'), ('patillas', 'Patillas'), ('penuelas', 'Penuelas'), ('ponce', 'Ponce'), ('quebradillas', 'Quebradillas'), ('rincon', 'Rincón'), ('rio_grande', 'Río Grande'), ('sabana_grande', 'Sabana Grande'), ('salinas', 'Salinas'), ('san_german', 'San German'), ('san_juan', 'San Juan'), ('san_lorenzo', 'San Lorenzo'), ('san_sebastian', 'San Sebastian'), ('santa_isabel', 'Santa Isabel'), ('toa_alta', 'Toa Alta'), ('toa_baja', 'Toa Baja'), ('trujillo_alto', 'Trujillo Alto'), ('utuado', 'Utuado'), ('vega_alta', 'Vega Alta'), ('vega_baja', 'Vega Baja'), ('vieques', 'Vieques'), ('villalba', 'Villalba'), ('yabucoa', 'Yabucoa'), ('yauco', 'Yauco')], max_length=255), default=list, size=None)),
                ('entity_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('any', 'Cualquier'), ('non_profit', 'Organización sin fines de lucro'), ('for_profit', 'Corporación o Asociación con fines de lucro '), ('sole_proprietor', 'Individuo (DBA-HNC)'), ('cooperative', 'Cooperativa')], max_length=255), default=list, size=None)),
                ('industries', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('any', 'Cualquiera'), ('11', '11 - Agricultura, Silvicultura, Caza y Pesca'), ('21', '21 - Extracción de Gas y Petróleo'), ('22', '22 - Utilidades'), ('23', '23 - Construcción'), ('31-33', '31-33 Manufactura'), ('42', '42 - Comercio al por mayor'), ('44-45', '44-45 - Comercio al por menor'), ('48-49', '48-49 - Transporte y Almacén'), ('51', '51 - Información'), ('52', '52 - Finanzas y Seguros'), ('53', '53 - Bienes Raíces, Alquiler y Arrendamiento'), ('54', '54 - Servicios profesionales, científicos y técnicos'), ('56', '56 - Administración y apoyo, central de desechos y servicios de reparación'), ('61', '61 - Servicios educativos'), ('62', '62 - Cuidados de salud y asistencia social'), ('71', '71 - Artes, Entretenimiento y Recreación'), ('72', '72 - Alojamiento, Servicios de Alimentos y Lugares para Beber'), ('81', '81 - Otros Servicios (exceptuando la administración pública)'), ('92', '92 - Administración Pública'), ('other', 'Otra')], max_length=255), default=list, size=None)),
                ('demographics', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('any', 'cualquiera'), ('student', 'estudiante'), ('veteran', 'veterano'), ('minority', 'minoría')], max_length=255), blank=True, default=list, size=None)),
                ('benefit_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('incentive', 'Incentivos'), ('loan', 'Créditos'), ('grant', 'Becas'), ('reimbursement', 'Reembolsos'), ('expertise', 'Talleres'), ('financing', 'Financiamiento'), ('other', 'Otros')], max_length=255), default=list, size=None)),
                ('purpose', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('anything', 'Cualquiera'), ('open_location', 'Abrir un Nuevo Local'), ('open_franchise', 'Abrir una Franquicia'), ('train_employees', 'Adiestrar Empleados'), ('working_capital', 'Capital de trabajo'), ('buy_equipment', 'Comprar Equipo'), ('buy_commercial_property', 'Comprar una propiedad comercial'), ('hire_employees', 'Contratar Empleados  / Pasantes'), ('start_business', 'Crear un Negocio'), ('export', 'Exportar'), ('export_products', 'Exportar productos'), ('export_services', 'Exportar servicios'), ('improve_commercial_property', 'Mejorar una propiedad comercial'), ('cinematographic_production', 'Producción Cinematográfica'), ('keep_employees', 'Retener empleados'), ('relocate_business', 'Reubicar un Negocio'), ('other', 'Otro (Por favor especifíca el propósito)')], max_length=255), default=list, size=None)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primerpeso.Agency')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Opportunities',
                'verbose_name': 'Opportunity',
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('provider', models.CharField(blank=True, max_length=255)),
                ('link', models.TextField(blank=True)),
                ('cost', models.TextField(blank=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Requirements',
                'verbose_name': 'Requirement',
            },
        ),
        migrations.CreateModel(
            name='RequirementRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primerpeso.Opportunity')),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primerpeso.Requirement')),
            ],
            options={
                'verbose_name_plural': 'Requirement Relationships',
                'verbose_name': 'Requirement Relationship',
            },
        ),
        migrations.AddField(
            model_name='opportunity',
            name='requirement',
            field=models.ManyToManyField(through='primerpeso.RequirementRelationship', to='primerpeso.Requirement'),
        ),
    ]
