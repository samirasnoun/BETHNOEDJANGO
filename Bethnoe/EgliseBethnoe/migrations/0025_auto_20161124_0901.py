# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-24 08:01
from __future__ import unicode_literals

import EgliseBethnoe.models
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EgliseBethnoe', '0024_chapitre_lien_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priere',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]