# Generated by Django 3.2.8 on 2021-11-08 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo', models.FloatField()),
                ('estado', models.CharField(max_length=20)),
                ('peso_paquete', models.FloatField()),
                ('documento_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.perfil_funcionario', verbose_name='documento_funcionario')),
                ('numero_entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.entidad', verbose_name='numero_entidad')),
            ],
        ),
    ]
