# Generated by Django 3.2.11 on 2022-02-04 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeshop_App', '0012_auto_20220203_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=15, null=True)),
                ('address_details', models.CharField(blank=True, max_length=50, null=True)),
                ('opening_date', models.CharField(blank=True, max_length=20, null=True)),
                ('opening_hours', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
