# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-03-02 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20200223_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='sidebar',
            name='status',
            field=models.IntegerField(choices=[(1, '\u5c55\u793a'), (2, '\u4e0b\u7ebf')], default=1, verbose_name='\u72b6\u6001'),
        ),
    ]
