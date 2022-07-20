# Generated by Django 3.2.8 on 2022-03-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeshop_App', '0041_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.RemoveField(
            model_name='billing_details',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='billing_details',
            name='cash_on_delivery',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='billing_details',
            name='direct_bank_payment',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='billing_details',
            name='paypal_payment',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
