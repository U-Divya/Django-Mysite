# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-18 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0011_auto_20180418_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published',
            field=models.DateField(),
        ),
    ]
