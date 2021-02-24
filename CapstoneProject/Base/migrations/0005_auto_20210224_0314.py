# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-02-23 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0004_auto_20210224_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentfinancialmodel',
            name='assets_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='presentfinancialmodel',
            name='assets_valuation',
            field=models.FloatField(blank=True),
        ),
    ]
