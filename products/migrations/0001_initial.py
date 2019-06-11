# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(default=9.99, max_digits=100, decimal_places=2)),
                ('sale_price', models.DecimalField(default=15.99, max_digits=100, decimal_places=2)),
            ],
        ),
    ]
