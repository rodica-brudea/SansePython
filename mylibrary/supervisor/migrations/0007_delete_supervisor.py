# Generated by Django 4.2.7 on 2023-12-09 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_alter_mysongs_mel'),
        ('supervisor', '0006_remove_supervisor_melodie_alter_supervisor_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Supervisor',
        ),
    ]