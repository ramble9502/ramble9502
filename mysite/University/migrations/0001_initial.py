# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-16 03:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6a19\u984c')),
                ('created_time', models.CharField(max_length=50, verbose_name='\u5b78\u5e74\u5ea6')),
            ],
            options={
                'db_table': 'CoursePlan',
                'verbose_name': '\u4e0a\u50b3\u8ab2\u7a0b\u898f\u5283',
                'verbose_name_plural': '\u8ab2\u7a0b\u898f\u5283',
            },
        ),
        migrations.CreateModel(
            name='Curriculum2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6a19\u984c')),
                ('created_time', models.CharField(max_length=50, verbose_name='\u5b78\u5e74\u5ea6')),
            ],
            options={
                'db_table': 'Curriculum2',
                'verbose_name': '\u4e0a\u50b3\u5b78\u671f\u8ab2\u8868',
                'verbose_name_plural': '\u5b78\u671f\u8ab2\u8868',
            },
        ),
        migrations.CreateModel(
            name='StudentCorner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6a19\u984c')),
            ],
            options={
                'db_table': 'StudentCorner',
                'verbose_name': '\u4e0a\u50b3\u5b78\u751f\u5712\u5730',
                'verbose_name_plural': '\u5b78\u751f\u5712\u5730',
            },
        ),
        migrations.CreateModel(
            name='Upload_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='university/file', verbose_name='\u9644\u4ef6\u6a94\u68481\uff1a')),
                ('file2', models.FileField(blank=True, upload_to='university/file', verbose_name='\u9644\u4ef6\u6a94\u68482\uff1a')),
                ('filename', models.CharField(blank=True, max_length=50, verbose_name='\u9644\u4ef6\u6a94\u6848\u540d\u7a31')),
            ],
        ),
        migrations.CreateModel(
            name='CoursePlan_Upload',
            fields=[
                ('upload_file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='University.Upload_File')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseupload', to='University.CoursePlan')),
            ],
            options={
                'db_table': 'CoursePlan_Upload',
                'verbose_name_plural': '\u8ab2\u7a0b\u898f\u5283\u6a94\u6848',
            },
            bases=('University.upload_file',),
        ),
        migrations.CreateModel(
            name='Curriculum_Upload',
            fields=[
                ('upload_file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='University.Upload_File')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curriculumupload', to='University.Curriculum2')),
            ],
            options={
                'db_table': 'Curriculum_Upload',
                'verbose_name_plural': '\u5b78\u671f\u8ab2\u8868\u6a94\u6848',
            },
            bases=('University.upload_file',),
        ),
        migrations.CreateModel(
            name='StudentCorner_Upload',
            fields=[
                ('upload_file_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='University.Upload_File')),
                ('image1', models.ImageField(blank=True, default='', upload_to=b'', verbose_name='\u5716\u72471')),
                ('image2', models.ImageField(blank=True, default='', upload_to=b'', verbose_name='\u5716\u72472')),
                ('image3', models.ImageField(blank=True, default='', upload_to=b'', verbose_name='\u5716\u72473')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cornerupload', to='University.StudentCorner')),
            ],
            options={
                'db_table': 'StudentCorner_Upload',
                'verbose_name_plural': '\u5b78\u751f\u5712\u5730\u8cc7\u6599\u4e0a\u50b3',
            },
            bases=('University.upload_file',),
        ),
    ]
