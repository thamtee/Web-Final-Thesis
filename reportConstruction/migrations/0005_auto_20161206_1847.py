# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportConstruction', '0004_auto_20161206_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportconstruction',
            name='status',
            field=models.CharField(choices=[('W', 'Working'), ('F', 'Finish'), ('L', 'Leave'), ('U', 'Unknown')], default='', max_length=5),
        ),
    ]
