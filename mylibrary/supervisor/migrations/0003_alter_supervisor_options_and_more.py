# Generated by Django 4.2.7 on 2023-12-09 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0002_supervisor_mel_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supervisor',
            options={'managed': True},
        ),
        migrations.RenameField(
            model_name='supervisor',
            old_name='mel_id',
            new_name='melodie',
        ),
        migrations.AlterModelTable(
            name='supervisor',
            table='usersongs',
        ),
    ]
