# Generated by Django 4.2.7 on 2023-12-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervisor',
            name='mel_id',
            field=models.IntegerField(default=1),
        ),
    ]
