# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_product_top'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_bottom',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='product.Product_bottom'),
            preserve_default=False,
        ),
    ]
