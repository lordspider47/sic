# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-02 05:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Catalogo',
                'verbose_name_plural': 'Catalogos',
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('codigo', models.IntegerField()),
                ('naturaleza', models.CharField(max_length=30)),
                ('debe', models.FloatField()),
                ('haber', models.FloatField()),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
            },
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField(max_length=500)),
                ('monto', models.FloatField()),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistemacontable.Cuenta')),
            ],
            options={
                'verbose_name': 'Partida',
                'verbose_name_plural': 'Partidas',
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partidas', models.ManyToManyField(to='sistemacontable.Partida')),
            ],
            options={
                'verbose_name': 'Periodo',
                'verbose_name_plural': 'Periodos',
            },
        ),
        migrations.AddField(
            model_name='catalogo',
            name='cuentas',
            field=models.ManyToManyField(to='sistemacontable.Cuenta'),
        ),
    ]
