# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document_title', models.CharField(max_length=100)),
                ('document_desc', models.CharField(max_length=100)),
                ('docfile', models.FileField(upload_to=b'media')),
            ],
        ),
    ]
