# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-13 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parceiro',
            name='link',
            field=models.CharField(default='link', max_length=1000),
            preserve_default=False,
        ),
    ]