# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-25 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default='30', max_digits=6),
        ),
    ]