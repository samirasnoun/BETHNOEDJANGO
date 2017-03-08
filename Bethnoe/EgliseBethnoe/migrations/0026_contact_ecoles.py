# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-26 08:21
from __future__ import unicode_literals

import EgliseBethnoe.models
import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EgliseBethnoe', '0025_auto_20161124_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=64)),
                ('prenom', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('description', ckeditor.fields.RichTextField(default='')),
            ],
        ),

    ]