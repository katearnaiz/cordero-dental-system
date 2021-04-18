# Generated by Django 3.1.7 on 2021-04-16 10:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(default=None, max_length=40)),
                ('contact_number', models.CharField(default=None, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(default=None, max_length=100)),
                ('material_type', models.CharField(choices=[('Perishable', 'Perishable'), ('Non-Perishable', 'Non-Perishable')], max_length=25)),
                ('threshold_value_unit', models.CharField(default=None, max_length=10)),
                ('threshold_value', models.IntegerField(default=None)),
                ('current_quantity', models.IntegerField(default=0)),
                ('supply_status', models.CharField(choices=[('Low Supply', 'Low Supply'), ('In-Supply (Med)', 'In-Supply (Med)'), ('In-Supply (High)', 'In-Supply (High)')], default='Low Supply', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(default=None, max_length=25)),
                ('business_name', models.CharField(default=None, max_length=50)),
                ('contact_person', models.CharField(default=None, max_length=40, unique=True)),
                ('address1', models.CharField(default=None, max_length=40)),
                ('address2', models.CharField(default=None, max_length=40)),
                ('special_notes', models.TextField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Delivered_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_restock', models.IntegerField(default=None)),
                ('delivery_date', models.DateField(default=django.utils.timezone.now)),
                ('parcel_number', models.CharField(default=None, max_length=50)),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dentalapp.material')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dentalapp.supplier')),
            ],
        ),
    ]
