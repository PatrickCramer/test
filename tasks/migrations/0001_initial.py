# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('namelist', '0008_auto_20160414_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=200)),
                ('done', models.CharField(max_length=100)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='namelist.Name')),
            ],
        ),
    ]
