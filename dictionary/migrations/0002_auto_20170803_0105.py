# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-02 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diction',
            old_name='word_type',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='diction',
            name='meaning',
            field=models.TextField(),
        ),
    ]
