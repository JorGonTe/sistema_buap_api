# Generated by Django 5.0.2 on 2024-11-20 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_buap_api', '0003_alumnos_maestros'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maestros',
            name='edad',
        ),
    ]
