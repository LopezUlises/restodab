# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restodab', '0003_auto_20170623_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('categoria', models.CharField(max_length=2, choices=[(b'P', b'Postre'), (b'L', b'Lunch'), (b'G', b'Guarnicion'), (b'D', b'Breakfast'), (b'B', b'Bebida')])),
            ],
        ),
        migrations.DeleteModel(
            name='Bebida',
        ),
        migrations.DeleteModel(
            name='Breackfast',
        ),
        migrations.DeleteModel(
            name='Guarnicion',
        ),
        migrations.DeleteModel(
            name='Lanch',
        ),
        migrations.DeleteModel(
            name='Postre',
        ),
    ]
