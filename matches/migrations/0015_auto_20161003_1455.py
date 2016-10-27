# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-03 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0014_auto_20161003_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='result_team',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, related_name='match_result', to='team.Team'),
        ),
    ]
