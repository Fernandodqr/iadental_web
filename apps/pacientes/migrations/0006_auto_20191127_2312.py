# Generated by Django 2.2.7 on 2019-11-28 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0005_auto_20191127_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='clinicas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinicas.Clinica'),
        ),
    ]
