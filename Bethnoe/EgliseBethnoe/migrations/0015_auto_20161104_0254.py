# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-04 01:54
from __future__ import unicode_literals

import EgliseBethnoe.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EgliseBethnoe', '0014_auto_20161104_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cd',
            name='audios',
            field=models.ManyToManyField(related_name='liste', through='EgliseBethnoe.AudioDuCD', to='EgliseBethnoe.Audio'),
        ),
        migrations.AlterField(
            model_name='imageevenement',
            name='image',
            field=models.FileField(upload_to=EgliseBethnoe.models.audio_upload_files, verbose_name='Photo '),
        ),
        migrations.AlterField(
            model_name='indexeglisebethnoe',
            name='fond_ecran',
            field=models.FileField(upload_to=EgliseBethnoe.models.audio_upload_files, verbose_name='Fond d ecran'),
        ),
        migrations.AlterField(
            model_name='indexeglisebethnoe',
            name='logo',
            field=models.FileField(upload_to=EgliseBethnoe.models.audio_upload_files, verbose_name='Logo '),
        ),
    ]
