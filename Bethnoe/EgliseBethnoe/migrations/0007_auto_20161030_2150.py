# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-30 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EgliseBethnoe', '0006_auto_20161029_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageevenement',
            name='slug',
            field=models.SlugField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imageevenement',
            name='titre_image',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]