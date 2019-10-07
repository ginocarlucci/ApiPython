# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-07 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TpPythonApp', '0007_auto_20191007_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoriaPadre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='TpPythonApp.Categoria'),
        ),
    ]
