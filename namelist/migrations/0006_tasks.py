# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namelist', '0005_adress_img_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=200)),
                ('done', models.CharField(max_length=100)),
            ],
        ),
    ]
