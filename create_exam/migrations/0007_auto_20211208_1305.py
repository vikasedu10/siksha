# Generated by Django 3.2.9 on 2021-12-08 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_exam', '0006_auto_20211208_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='exam',
        ),
        migrations.AddField(
            model_name='exam',
            name='batch',
            field=models.ManyToManyField(blank=True, to='create_exam.Batch'),
        ),
    ]
