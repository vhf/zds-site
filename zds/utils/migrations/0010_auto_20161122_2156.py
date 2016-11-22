# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0009_auto_20161113_2328'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Licence',
            new_name='License',
        ),
        migrations.AlterModelOptions(
            name='license',
            options={'verbose_name': 'License', 'verbose_name_plural': 'Licenses'},
        ),
    ]
