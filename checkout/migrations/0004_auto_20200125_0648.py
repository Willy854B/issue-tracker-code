# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-25 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20200123_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default='30', max_digits=6),
        ),
    ]