# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-07-16 17:04
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Pilot', '0011_auto_20200716_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='option_1',
            field=otree.db.models.IntegerField(null=True, verbose_name='Option X'),
        ),
    ]
