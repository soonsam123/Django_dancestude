# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-11 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(max_length=10000),
        ),
    ]