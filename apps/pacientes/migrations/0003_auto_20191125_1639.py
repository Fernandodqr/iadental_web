# Generated by Django 2.2.7 on 2019-11-25 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dentista', '0001_initial'),
        ('clinicas', '0003_clinica_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacientes', '0002_auto_20191125_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='clinicas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clinicas.Clinica'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='dentistas',
            field=models.ManyToManyField(to='dentista.Dentista'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
