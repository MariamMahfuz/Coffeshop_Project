# Generated by Django 3.2.11 on 2022-03-16 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeshop_App', '0039_state_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing_details',
            name='payment_method',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
