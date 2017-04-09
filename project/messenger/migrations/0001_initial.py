# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 22:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.Properties')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messenger.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]