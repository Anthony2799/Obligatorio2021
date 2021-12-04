# Generated by Django 3.2.9 on 2021-12-04 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_remove_entidad_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='numero_grupo',
            field=models.CharField(choices=[('INITIATED', 'INITIATED'), ('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED'), ('FAILED', 'FAILED'), ('ERROR', 'ERROR')], max_length=50),
        ),
    ]
