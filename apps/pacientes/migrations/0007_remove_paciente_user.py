# Generated by Django 2.2.7 on 2019-12-01 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0006_auto_20191127_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='user',
        ),
    ]
