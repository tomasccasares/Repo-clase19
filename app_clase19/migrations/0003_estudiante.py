# Generated by Django 4.0.5 on 2022-07-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_clase19', '0002_rename_nombre_productos_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
