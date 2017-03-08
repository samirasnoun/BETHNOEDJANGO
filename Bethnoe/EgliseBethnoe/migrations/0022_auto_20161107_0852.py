# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EgliseBethnoe', '0021_dirigenteglisebethnoe_lien'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dirigenteglisebethnoe',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='dirigenteglisebethnoe',
            name='prenom',
        ),
        migrations.AlterField(
            model_name='dirigenteglisebethnoe',
            name='nom',
            field=models.CharField(blank=True, max_length=150, verbose_name='Nom de la section du site \xe0 mettre en valeur '),
        ),
        migrations.AlterField(
            model_name='dirigenteglisebethnoe',
            name='role',
            field=models.CharField(blank=True, max_length=250, verbose_name='Sous texte'),
        ),
    ]