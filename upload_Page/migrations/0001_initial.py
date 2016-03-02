# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, blank=True)),
                ('file', models.FileField(upload_to=b'/meida/')),
                ('upload_time', models.TimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Excel File',
                'verbose_name_plural': 'Excel File List',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rows',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(editable=False)),
                ('belong_to', models.ForeignKey(to='upload_Page.ExcelFile')),
            ],
            options={
                'verbose_name': 'Excel Rows',
                'verbose_name_plural': 'Excel Rows List',
            },
            bases=(models.Model,),
        ),
    ]
