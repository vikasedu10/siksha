# Generated by Django 3.2.8 on 2021-12-07 09:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('create_exam', '0002_auto_20211206_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]