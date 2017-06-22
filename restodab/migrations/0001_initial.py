# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('categoria', models.ForeignKey(to='restodab.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Guarnicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='comida',
            name='guarnicion',
            field=models.ForeignKey(to='restodab.Guarnicion'),
        ),
        migrations.AddField(
            model_name='bebida',
            name='categoria',
            field=models.ForeignKey(to='restodab.Categoria'),
        ),
    ]
