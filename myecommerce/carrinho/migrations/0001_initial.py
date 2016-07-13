# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
