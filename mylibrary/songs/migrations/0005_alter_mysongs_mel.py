# Generated by Django 4.2.7 on 2023-12-09 16:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0004_alter_mysongs_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysongs',
            name='mel',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
