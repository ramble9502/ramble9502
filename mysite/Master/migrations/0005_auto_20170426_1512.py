# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-26 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0004_auto_20170426_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bachelor_test',
            name='filetitle',
            field=models.CharField(choices=[('\u5b78\u4f4d\u8003\u8a66\u76f8\u95dc\u6a94\u6848\u4e0b\u8f09', '\u5b78\u4f4d\u8003\u8a66\u76f8\u95dc\u6a94\u6848\u4e0b\u8f09'), ('\u7814\u7a76\u8a08\u756b\u53e3\u8a66\u76f8\u95dc\u6a94\u6848', '\u7814\u7a76\u8a08\u756b\u53e3\u8a66\u76f8\u95dc\u6a94\u6848'), ('\u8ad6\u6587\u53e3\u8a66\u76f8\u95dc\u6a94\u6848', '\u8ad6\u6587\u53e3\u8a66\u76f8\u95dc\u6a94\u6848')], max_length=50, verbose_name='\u6a94\u6848\u985e\u5225'),
        ),
    ]
