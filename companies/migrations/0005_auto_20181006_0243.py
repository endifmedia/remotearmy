# Generated by Django 2.1.1 on 2018-10-06 02:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20181006_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='number_of_employees',
            field=models.CharField(choices=[('1-10 people', '1-10 people'), ('1-20 people', '1-20 people'), ('1-50 people', '1-50 people'), ('100+ people', '100+ people'), ('500+ people', '500+ people')], default='1-10 people', max_length=16),
        ),
        migrations.AlterField(
            model_name='company',
            name='year_founded',
            field=models.PositiveIntegerField(blank=True, default=None, help_text='Use the following format: <YYYY>', null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2018)]),
        ),
    ]
