# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WangyiArticle',
            fields=[
                ('docid', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('url', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('digest', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=50)),
                ('ptime', models.DateTimeField()),
                ('mtime', models.DateTimeField()),
                ('comments_url', models.CharField(max_length=200)),
                ('comments_number', models.IntegerField(default=0)),
                ('votecount', models.IntegerField(default=0)),
                ('replycount', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('parent_id', models.CharField(max_length=50)),
                ('url_3w', models.CharField(max_length=200)),
            ],
        ),
    ]
