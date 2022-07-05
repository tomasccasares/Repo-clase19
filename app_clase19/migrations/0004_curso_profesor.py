# Generated by Django 4.0.5 on 2022-07-05 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clase19', '0003_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('camada', models.IntegerField()),
                ('fechaDeInicio', models.DateField()),
                ('fechaDeFin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('profesion', models.CharField(max_length=30)),
                ('emial', models.EmailField(max_length=254)),
            ],
        ),
    ]