# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaikissan', '0003_auto_20170913_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='FF_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='W_Id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
