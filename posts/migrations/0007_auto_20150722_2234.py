# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20150722_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
