# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-22 12:10
from __future__ import unicode_literals

import EnseignementsBibliques.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnseignementsBibliques', '0005_auto_20180422_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enseignementbiblique',
            name='image',
            field=models.FileField(blank=True, default='', upload_to=EnseignementsBibliques.models.media_upload_files),
        ),
        migrations.AlterField(
            model_name='enseignementbiblique',
            name='media',
            field=models.FileField(blank=True, upload_to=EnseignementsBibliques.models.media_upload_files),
        ),
    ]