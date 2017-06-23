# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restodab', '0002_auto_20170622_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breackfast',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Guarnicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lanch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Postre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='comida',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='bebida',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Comida',
        ),
    ]
