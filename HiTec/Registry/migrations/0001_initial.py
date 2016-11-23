# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 13:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=1)),
                ('birth_date', models.DateTimeField(verbose_name='birth date')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.CharField(max_length=15)),
                ('max', models.IntegerField(default=10)),
                ('color', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='team_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registry.Team'),
        ),
    ]