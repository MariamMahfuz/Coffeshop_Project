# Generated by Django 3.2.11 on 2022-02-05 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeshop_App', '0019_best_selling_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_photo', models.ImageField(upload_to='media')),
                ('dish_heading', models.CharField(blank=True, max_length=50, null=True)),
                ('dish_description', models.CharField(blank=True, max_length=200, null=True)),
                ('dish_price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
