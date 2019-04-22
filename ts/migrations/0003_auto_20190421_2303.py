# Generated by Django 2.2 on 2019-04-21 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0002_remove_logthermostat_hum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logthermostat',
            name='on',
        ),
        migrations.AddField(
            model_name='logthermostat',
            name='light',
            field=models.BooleanField(default=False, verbose_name='Стан освітлення'),
        ),
        migrations.AddField(
            model_name='logthermostat',
            name='light_B',
            field=models.IntegerField(default=0, verbose_name='B'),
        ),
        migrations.AddField(
            model_name='logthermostat',
            name='light_G',
            field=models.IntegerField(default=0, verbose_name='G'),
        ),
        migrations.AddField(
            model_name='logthermostat',
            name='light_R',
            field=models.IntegerField(default=0, verbose_name='R'),
        ),
        migrations.AddField(
            model_name='logthermostat',
            name='set_co2',
            field=models.FloatField(blank=True, null=True, verbose_name='Встановлений рівень CO2'),
        ),
        migrations.AddField(
            model_name='logthermostat',
            name='set_temp',
            field=models.FloatField(default=0, verbose_name='Встановлена температура'),
        ),
        migrations.AddField(
            model_name='logthermostat',
            name='thermostat_state',
            field=models.BooleanField(default=False, verbose_name='Стан термостату'),
        ),
        migrations.AlterField(
            model_name='logthermostat',
            name='co2',
            field=models.FloatField(blank=True, null=True, verbose_name='Рівень CO2'),
        ),
        migrations.AlterField(
            model_name='logthermostat',
            name='temp',
            field=models.FloatField(default=0, verbose_name='Температура'),
        ),
    ]
