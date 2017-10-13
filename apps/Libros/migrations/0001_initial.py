# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Autores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('DIS', 'disponible'), ('AG', 'agotado')], default='DIS', max_length=2)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Autores.Autor')),
            ],
        ),
    ]
