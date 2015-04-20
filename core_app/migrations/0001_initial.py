# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(default='', max_length=255)),
                ('estado', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], default=2)),
            ],
            options={
                'ordering': ['estado'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Alarma',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(default='', max_length=255)),
                ('descripcion', models.CharField(default='', max_length=512)),
                ('activa', models.BooleanField(default=True)),
                ('notifica', models.BooleanField(default=True)),
                ('eliminada', models.BooleanField(default=False)),
                ('nivel_alarma', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], default=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlarmaAcceso',
            fields=[
                ('alarma_ptr', models.OneToOneField(serialize=False, parent_link=True, to='core_app.Alarma', auto_created=True, primary_key=True)),
                ('hora_inicio', models.TimeField(help_text='hh:mm:ss')),
                ('hora_fin', models.TimeField(help_text='hh:mm:ss')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.alarma',),
        ),
        migrations.CreateModel(
            name='AlarmaEstado',
            fields=[
                ('alarma_ptr', models.OneToOneField(serialize=False, parent_link=True, to='core_app.Alarma', auto_created=True, primary_key=True)),
                ('estado_sensor', models.BooleanField(default=True)),
                ('hora_inicio', models.TimeField(help_text='hh:mm:ss')),
                ('hora_fin', models.TimeField(help_text='hh:mm:ss')),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.alarma',),
        ),
        migrations.CreateModel(
            name='AlarmaHumo',
            fields=[
                ('alarma_ptr', models.OneToOneField(serialize=False, parent_link=True, to='core_app.Alarma', auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.alarma',),
        ),
        migrations.CreateModel(
            name='AlarmaReportada',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(default='', max_length=255)),
                ('descripcion', models.CharField(default='', max_length=512)),
                ('fecha_hora', models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 20, 0, 55, 21, 18536))),
                ('nivel_alerta', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], default=2)),
                ('leida', models.BooleanField(default=False)),
                ('alarma', models.ForeignKey(to='core_app.Alarma')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('activo_ptr', models.OneToOneField(serialize=False, parent_link=True, to='core_app.Activo', auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.activo',),
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(default='', max_length=255)),
                ('codigo', models.CharField(max_length=10)),
                ('trama', models.CharField(max_length=1000)),
                ('fecha_hora_evento', models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 20, 0, 55, 21, 15591))),
                ('fecha_hora_sistema', models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 20, 0, 55, 21, 15631))),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoryAlarmas',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('estado', models.BooleanField(default=True)),
                ('fecha', models.DateTimeField()),
                ('alarma', models.ForeignKey(to='core_app.Alarma')),
                ('elemento', models.ForeignKey(to='core_app.Elemento')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('activo_ptr', models.OneToOneField(serialize=False, parent_link=True, to='core_app.Activo', auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('core_app.activo',),
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(default='', max_length=255)),
                ('activo', models.ForeignKey(to='core_app.Elemento')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoSensor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(default='', max_length=255)),
                ('descripcion', models.CharField(default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sensor',
            name='tipo_sensor',
            field=models.ForeignKey(to='core_app.TipoSensor', default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inmueble',
            name='proyecto',
            field=models.ForeignKey(to='core_app.Proyecto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='historyalarmas',
            name='inmueble',
            field=models.ForeignKey(to='core_app.Inmueble'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='historyalarmas',
            name='sensor',
            field=models.ForeignKey(to='core_app.Sensor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evento',
            name='sensor',
            field=models.ForeignKey(to='core_app.Sensor', default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='elemento',
            name='inmueble',
            field=models.ForeignKey(to='core_app.Inmueble'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alarma',
            name='sensor',
            field=models.ForeignKey(to='core_app.Sensor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activo',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
