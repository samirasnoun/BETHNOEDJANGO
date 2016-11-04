# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-03 22:34
from __future__ import unicode_literals

import EgliseBethnoe.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EgliseBethnoe', '0012_cultehebdo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=250)),
                ('audio', models.FileField(upload_to=EgliseBethnoe.models.audio_upload_files)),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='AudioDuCD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_cd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EgliseBethnoe.Audio')),
            ],
        ),
        migrations.CreateModel(
            name='CD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=250)),
                ('slug', models.SlugField()),
                ('audio', models.ManyToManyField(through='EgliseBethnoe.AudioDuCD', to='EgliseBethnoe.Audio')),
            ],
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
        migrations.AddField(
            model_name='audioducd',
            name='cd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EgliseBethnoe.CD'),
        ),
    ]
