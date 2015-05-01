# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UeditorFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='deleted at', blank=True)),
                ('name', models.CharField(max_length=255, verbose_name='filename')),
                ('type', models.CharField(max_length=255, null=True, verbose_name='file type', blank=True)),
                ('url', models.CharField(max_length=255, null=True, verbose_name='url', blank=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
            },
        ),
    ]
