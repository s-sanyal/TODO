# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-21 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_auto_20180821_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='todo',
            field=models.ManyToManyField(to='todoapp.Todo'),
        ),
        migrations.AlterField(
            model_name='group',
            name='invite_link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]