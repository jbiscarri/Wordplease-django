# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.TextField(default=b'')),
                ('body', models.TextField(default=b'')),
                ('url', models.URLField()),
                ('publish_date', models.DateTimeField()),
            ],
        ),
    ]
