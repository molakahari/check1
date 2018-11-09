# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrb', '0002_hotelusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('roomtype', models.CharField(choices=[('ac', 'AC'), ('nonac', 'NonAc')], default='ac', max_length=6)),
                ('bedtype', models.CharField(choices=[('single', 'SINGLE'), ('double', 'DOUBLE')], default='single', max_length=7)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
