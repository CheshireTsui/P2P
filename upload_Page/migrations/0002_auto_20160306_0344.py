# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_Page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelfile',
            name='file',
            field=models.FileField(upload_to=b'meida/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='excelfile',
            name='upload_time',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
