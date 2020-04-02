# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-02 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='choice',
            field=models.CharField(choices=[('all_mountain', 'All Mountain'), ('big_mountain', 'Big Mountain'), ('freestyle', 'Freestyle'), ('pipe_park', 'Pipe/Park'), ('jib_street', 'Jib/Street'), ('boardercross', 'Boardercross')], default='All Mountain', max_length=50),
        ),
    ]
