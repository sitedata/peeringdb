# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-19 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peeringdb_server', '0006_network_allow_ixp_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='ixlan',
            name='json_member_list_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
