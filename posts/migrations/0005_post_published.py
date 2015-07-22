# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
