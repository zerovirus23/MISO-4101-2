# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarmareportada',
            name='fecha_hora',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 15, 5, 15, 24, 669346)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_hora_evento',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 15, 5, 15, 24, 666931)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_hora_sistema',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 15, 5, 15, 24, 666958)),
            preserve_default=True,
        ),
    ]