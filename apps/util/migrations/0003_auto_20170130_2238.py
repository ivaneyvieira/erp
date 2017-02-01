# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0002_cidade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cidade',
            options={'verbose_name': 'Cidade', 'verbose_name_plural': 'Cidades'},
        ),
        migrations.AlterModelOptions(
            name='estado',
            options={'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterModelOptions(
            name='regiao',
            options={'verbose_name': 'Região', 'verbose_name_plural': 'Regiões'},
        ),
        migrations.AlterField(
            model_name='regiao',
            name='nome',
            field=models.CharField(max_length=20, verbose_name='Nome da Região'),
        ),
        migrations.AlterField(
            model_name='regiao',
            name='sigla',
            field=models.CharField(help_text='Sigla do estado', max_length=2, unique=True, verbose_name='Sigla'),
        ),
    ]
