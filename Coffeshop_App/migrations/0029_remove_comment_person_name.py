# Generated by Django 3.2.8 on 2022-02-06 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeshop_App', '0028_auto_20220207_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='person_name',
        ),
    ]