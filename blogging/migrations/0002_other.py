# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-16 05:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_in', models.CharField(max_length=30)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogging.Blog')),
            ],
        ),
    ]