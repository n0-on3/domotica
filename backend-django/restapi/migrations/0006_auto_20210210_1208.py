# Generated by Django 3.1.6 on 2021-02-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_auto_20210210_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thermostat',
            name='actual_temperature',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='thermostat',
            name='temperature_set',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
    ]
