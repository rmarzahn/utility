# Generated by Django 2.0.13 on 2019-07-15 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20190715_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletteruser',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Benutzername (optional)'),
        ),
    ]
