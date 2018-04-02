# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-02 21:45
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0008_auto_20180329_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='entity_meta',
            field=django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
    ]
