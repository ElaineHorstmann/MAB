# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-07-15 18:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pilot', '0005_remove_player_draws_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='draws_2',
        ),
        migrations.RemoveField(
            model_name='player',
            name='draws_3',
        ),
    ]
