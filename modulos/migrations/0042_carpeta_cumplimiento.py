# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-03 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0041_auto_20171102_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpeta',
            name='cumplimiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='run', to='modulos.Ejecucion'),
        ),
    ]
