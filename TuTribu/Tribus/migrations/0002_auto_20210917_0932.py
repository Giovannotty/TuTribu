# Generated by Django 3.2.7 on 2021-09-17 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tribus', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Eventos',
            new_name='Evento',
        ),
        migrations.RenameModel(
            old_name='Tribus',
            new_name='Tribu',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='tribus_ptr',
            new_name='tribu_ptr',
        ),
    ]
