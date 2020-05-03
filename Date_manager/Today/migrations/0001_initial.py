# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2020-05-02 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Today',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('event_date', models.DateField()),
                ('crate_date', models.DateField(auto_now_add=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]
