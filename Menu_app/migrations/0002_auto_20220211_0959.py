# Generated by Django 3.2.11 on 2022-02-11 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessert',
            name='dessert_descripion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='drinks',
            name='drinks_descripion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='maindish',
            name='main_dish_descripion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='starter',
            name='starter_descripion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]