# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oldConstruction', '0002_oldconstruction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oldconstruction',
            name='category',
            field=models.CharField(choices=[('ถนน', 'ถนน'), ('สะพาน', 'สะพาน'), ('รถไฟ', 'รถไฟ'), ('อาคาร', 'อาคาร'), ('วางท่อระบายน้ำ', 'วางท่อระบายน้ำ'), ('เขื่อน', 'เขื่อน'), ('อ่างเก็บน้ำ', 'อ่างเก็บน้ำ'), ('บ่อบำบัดน้ำ', 'บ่อบำบัดน้ำ'), ('คลอง', 'คลอง')], default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='oldconstruction',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='oldconstruction',
            name='status',
            field=models.CharField(choices=[('W', 'Working'), ('F', 'Finish'), ('L', 'Leave'), ('U', 'Unknown')], max_length=1),
        ),
    ]
