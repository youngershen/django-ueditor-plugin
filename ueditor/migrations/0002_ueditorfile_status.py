# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ueditor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ueditorfile',
            name='status',
            field=models.IntegerField(default=0, verbose_name='status', choices=[(0, 'upload succeed'), (1, 'upload failed')]),
        ),
    ]
