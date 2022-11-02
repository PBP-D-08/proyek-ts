# Generated by Django 4.1 on 2022-11-02 04:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='description',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(38)]),
        ),
    ]
