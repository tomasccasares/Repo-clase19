# Generated by Django 4.0.5 on 2022-07-01 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_clase19', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='nombre',
            new_name='producto',
        ),
    ]
