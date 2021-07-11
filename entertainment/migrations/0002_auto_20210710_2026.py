# Generated by Django 3.2.5 on 2021-07-10 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='preview',
            new_name='imageUrl',
        ),
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.CharField(blank=True, max_length=200, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(blank=True, max_length=200, unique=True, verbose_name='Название видео'),
        ),
    ]
