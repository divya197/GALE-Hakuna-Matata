# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_app', '0004_auto_20170624_0424'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='seq',
            field=models.IntegerField(help_text='All actions of a particular usecase are executed in the order of this sequence number.', null=True, verbose_name='Sequence Number'),
        ),
    ]