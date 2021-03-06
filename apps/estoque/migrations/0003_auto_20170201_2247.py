# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_auto_20170131_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=4, max_digits=15)),
            ],
            options={
                'verbose_name': 'Estoque',
                'verbose_name_plural': 'Estoques',
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('data_validade', models.DateField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Produto')),
            ],
            options={
                'verbose_name': 'Lote',
                'verbose_name_plural': 'Lotes',
            },
        ),
        migrations.CreateModel(
            name='Prateleira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Categoria')),
            ],
            options={
                'verbose_name': 'Prateleira',
                'verbose_name_plural': 'Prateleiras',
            },
        ),
        migrations.AddField(
            model_name='estoque',
            name='lote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Lote'),
        ),
        migrations.AddField(
            model_name='estoque',
            name='pratieleira',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Prateleira'),
        ),
        migrations.AlterUniqueTogether(
            name='estoque',
            unique_together=set([('lote', 'pratieleira')]),
        ),
    ]
