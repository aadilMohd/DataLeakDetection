# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_logindetails_clientid'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindetails',
            name='cipher_text',
            field=models.CharField(default='xyz', max_length=25),
        ),
        migrations.AddField(
            model_name='logindetails',
            name='hash_text',
            field=models.CharField(default='xyz', max_length=65),
        ),
    ]