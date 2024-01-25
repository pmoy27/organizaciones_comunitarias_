# Generated by Django 5.0.1 on 2024-01-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_directiva', models.CharField(max_length=15, unique=True)),
                ('tipo_de_organizacion', models.CharField(max_length=100, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('rol_municipalidad', models.IntegerField(unique=True)),
                ('fecha_concesion_p_j', models.DateField()),
                ('numero_inscripcion_rc', models.IntegerField(unique=True)),
                ('sede_lugar_funcionamiento', models.CharField(max_length=100)),
                ('directiva', models.CharField(max_length=100)),
                ('vigencia_directiva', models.CharField(max_length=100)),
                ('estatuto', models.DateField()),
                ('fecha_termino_directiva', models.DateField()),
            ],
        ),
    ]