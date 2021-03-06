# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-29 12:10
from __future__ import unicode_literals

import EgliseBethnoe.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EgliseBethnoe', '0004_indexeglisebethnoe_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexeglisebethnoe',
            name='fond_ecran',
            field=models.FileField(default='', upload_to=EgliseBethnoe.models.audio_upload_files, verbose_name='Fond d ecran'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='indexeglisebethnoe',
            name='logo',
            field=models.FileField(upload_to=EgliseBethnoe.models.audio_upload_files, verbose_name='Logo '),
        ),
    ]
