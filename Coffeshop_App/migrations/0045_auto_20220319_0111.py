# Generated by Django 3.2.11 on 2022-03-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffeshop_App', '0044_auto_20220318_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('email_address', models.EmailField(max_length=254, null=True)),
                ('website', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email_address', models.EmailField(max_length=254, null=True)),
                ('subject', models.CharField(max_length=150, null=True)),
                ('message', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='Product_detail',
            field=models.CharField(max_length=5000),
        ),
    ]
