# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='landing.Cliente')),
                ('productos', models.ManyToManyField(to='landing.Producto')),
            ],
        ),
    ]
