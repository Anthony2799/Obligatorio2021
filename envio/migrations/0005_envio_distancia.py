# Generated by Django 3.2.8 on 2021-12-05 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envio', '0004_alter_envio_costo'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio',
            name='distancia',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
