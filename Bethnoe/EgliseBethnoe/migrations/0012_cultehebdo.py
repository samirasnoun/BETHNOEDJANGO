# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-01 14:47
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EgliseBethnoe', '0011_evenement_type_evenments'),
    ]

    operations = [
        migrations.CreateModel(
            name='CulteHebdo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Titre Culte Hebdomadaire : ')),
                ('content', ckeditor.fields.RichTextField()),
                ('video_url', models.URLField(verbose_name='Url de la video du culte hebdomadaire')),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
    ]
