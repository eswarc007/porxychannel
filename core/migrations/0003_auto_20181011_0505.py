# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-10-11 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_proxies'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proxies',
            options={'verbose_name': 'proxy', 'verbose_name_plural': 'proxies'},
        ),
        migrations.AlterField(
            model_name='proxies',
            name='ports',
            field=models.CharField(max_length=100),
        ),
    ]