# Generated by Django 4.2 on 2023-04-21 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestorapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantel',
            old_name='campus',
            new_name='carreras',
        ),
    ]
