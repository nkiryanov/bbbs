# Generated by Django 3.2.5 on 2021-07-07 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0006_merge_20210707_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.DurationField(null=True, verbose_name='Продолжительность видео'),
        ),
    ]
