# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-06-09 11:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Investment', '0002_auto_20210609_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='investmentRiskLiquidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk', models.IntegerField()),
                ('liquidity', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='investmentdivision',
            name='liquidity',
        ),
        migrations.RemoveField(
            model_name='investmentdivision',
            name='risk',
        ),
    ]
