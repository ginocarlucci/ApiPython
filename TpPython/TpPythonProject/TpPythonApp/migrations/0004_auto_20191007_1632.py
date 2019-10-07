# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-07 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TpPythonApp', '0003_auto_20191007_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoriaPadre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoria_hija', to='TpPythonApp.Categoria'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='categorias',
            field=models.ManyToManyField(related_name='categorias_habilitadas', to='TpPythonApp.Categoria'),
        ),
        migrations.AlterField(
            model_name='precio',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TpPythonApp.Producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos_categoria', to='TpPythonApp.Categoria'),
        ),
    ]
