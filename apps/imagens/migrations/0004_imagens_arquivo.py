# Generated by Django 2.2.7 on 2019-11-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagens', '0003_auto_20191125_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagens',
            name='arquivo',
            field=models.FileField(default=1, upload_to='imagens'),
            preserve_default=False,
        ),
    ]