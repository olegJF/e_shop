# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-13 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def fill_status_fild(apps, _):
    fields = [('new', 'Новый'), ('pending', 'Обрабатывается'),
             ('canceled', 'Отменен'), ('delivered', 'Доставлен'),]
    status = apps.get_model('cart', 'Status')
    for key, val in fields:
        st = status.objects.create(slug=key, name=val)

        
class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [

        migrations.RunPython(fill_status_fild),
    ]
