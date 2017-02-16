# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_type', models.CharField(max_length=20)),
                ('brief_desc', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'wheretonow_place_categories',
            },
        ),
    ]
