# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialv2', '0014_auto_20160331_0415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publishablecontent',
            old_name='licence',
            new_name='license',
        ),
    ]
