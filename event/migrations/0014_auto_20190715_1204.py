# Generated by Django 2.0.13 on 2019-07-15 10:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_auto_20190715_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date Format (tt.mm.jjjj)'),
        ),
    ]
