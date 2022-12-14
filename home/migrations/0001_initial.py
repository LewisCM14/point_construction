# Generated by Django 3.2 on 2022-10-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=16, unique=True)),
                ('street_address1', models.CharField(max_length=80, unique=True)),
                ('street_address2', models.CharField(max_length=80, unique=True)),
                ('town_or_city', models.CharField(max_length=40, unique=True)),
                ('postcode', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Company Details',
            },
        ),
    ]
