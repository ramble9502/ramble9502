# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-18 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityNews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linkactivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activitytitle', models.CharField(max_length=100, verbose_name='\u76f8\u95dc\u9023\u7d50\u6a19\u984c')),
                ('link', models.URLField(blank=True, verbose_name='\u76f8\u95dc\u9023\u7d50')),
            ],
            options={
                'db_table': 'Linkactivity',
                'verbose_name': '\u4e0a\u50b3\u76f8\u95dc\u9023\u7d50',
                'verbose_name_plural': '\u76f8\u95dc\u9023\u7d50',
            },
        ),
        migrations.CreateModel(
            name='Linkindex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=100, verbose_name='\u76f8\u95dc\u6c42\u8077\u8a0a\u606f\u6a19\u984c')),
                ('link', models.URLField(blank=True, verbose_name='\u6c42\u8077\u9023\u7d50')),
            ],
            options={
                'db_table': 'Linkindex',
                'verbose_name': '\u4e0a\u50b3\u6c42\u8077\u8a0a\u606f',
                'verbose_name_plural': '\u6c42\u8077\u8a0a\u606f',
            },
        ),
    ]
