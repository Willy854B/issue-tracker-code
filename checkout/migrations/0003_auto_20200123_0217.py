# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-23 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20191225_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
