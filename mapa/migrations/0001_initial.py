# Generated by Django 3.2.9 on 2021-11-09 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_zona', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo_distribuidora',
            fields=[
                ('matricula', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('estado_vehiculo', models.CharField(max_length=20)),
                ('capacidad', models.FloatField()),
                ('nro_zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapa.zona', verbose_name='id')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion_zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
                ('nro_zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapa.zona', verbose_name='id')),
            ],
        ),
    ]
