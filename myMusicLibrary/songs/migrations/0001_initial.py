# Generated by Django 5.0 on 2023-12-22 16:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MySongs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_path', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('mel', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'mysongs',
                'managed': True,
            },
        ),
    ]