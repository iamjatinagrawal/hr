# Generated by Django 2.2.5 on 2020-03-27 07:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0004_auto_20200327_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]
