# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20160106_2231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchindexcontent',
            old_name='licence',
            new_name='license',
        ),
    ]
