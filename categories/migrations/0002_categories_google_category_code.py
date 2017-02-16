# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='google_category_code',
            field=models.CharField(default=b'google_place_code', max_length=20),
        ),
    ]
