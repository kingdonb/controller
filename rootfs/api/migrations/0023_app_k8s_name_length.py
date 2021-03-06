# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 22:15
from __future__ import unicode_literals

import api.models.app
import api.models.certificate
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_add_private_key_validation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='id',
            field=models.SlugField(max_length=63, null=True, unique=True, validators=[api.models.app.validate_app_id, api.models.app.validate_reserved_names]),
        ),
    ]
