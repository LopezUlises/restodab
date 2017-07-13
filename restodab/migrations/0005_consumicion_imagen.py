# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restodab', '0004_auto_20170711_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumicion',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'static/img', blank=True),
        ),
    ]
