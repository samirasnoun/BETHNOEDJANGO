# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-03 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EgliseBethnoe', '0006_auto_20161002_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextDirigentEgliseBethnoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=50)),
                ('texte', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]
