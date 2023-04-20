# Generated by Django 4.2 on 2023-04-20 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('semestres', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Plantel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_institucion', models.CharField(max_length=255)),
                ('campus', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('materia', models.CharField(max_length=255)),
                ('carrera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.carrera')),
                ('domicilio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.domicilio')),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('semestre', models.IntegerField()),
                ('carrera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.carrera')),
                ('domicilio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestorapp.domicilio')),
            ],
        ),
    ]
