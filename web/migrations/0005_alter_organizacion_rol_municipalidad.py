# Generated by Django 5.0.1 on 2024-01-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_organizacion_tipo_de_organizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='rol_municipalidad',
            field=models.IntegerField(),
        ),
    ]
