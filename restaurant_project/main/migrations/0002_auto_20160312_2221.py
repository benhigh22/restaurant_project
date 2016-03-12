# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='item',
        ),
        migrations.AddField(
            model_name='menu',
            name='item',
            field=models.ManyToManyField(to='main.Item'),
        ),
    ]
