# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 21:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('triageWeb', '0003_auto_20160502_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='report_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 2, 21, 13, 24, 947235, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
