# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-12 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parceiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('local', models.CharField(max_length=300)),
                ('logo', models.FileField(default='inicial/static/img/logo.png', upload_to='')),
            ],
        ),
    ]