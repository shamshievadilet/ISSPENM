# Generated by Django 2.2.1 on 2019-05-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_auto_20190513_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminals',
            name='check',
            field=models.BooleanField(default=False, verbose_name='Подтверждение'),
        ),
    ]
