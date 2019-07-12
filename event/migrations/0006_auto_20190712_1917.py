# Generated by Django 2.0.13 on 2019-07-12 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20190712_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Format: dd.mm.jjjj'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, help_text='Format: --:--'),
        ),
    ]
