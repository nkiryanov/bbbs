# Generated by Django 3.2.4 on 2021-06-20 19:29

from django.db import migrations, models

import places.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen', models.BooleanField(default=False, verbose_name='Выбор наставника')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Мальчик'), ('F', 'Девочка')], max_length=1, null=True, verbose_name='Пол')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Возраст')),
                ('activity_type', models.PositiveSmallIntegerField(choices=[(0, 'Активный'), (1, 'Развлекательный'), (2, 'Познавательный')], verbose_name='Тип отдыха')),
                ('description', models.TextField(help_text='Поделитесь впечатлениями о проведенном времени', verbose_name='Комментарий')),
                ('link', models.URLField(blank=True, help_text='Введите адрес сайта', null=True, verbose_name='Сайт')),
                ('imageUrl', models.ImageField(blank=True, help_text='Добавить фото', null=True, upload_to=places.models.get_upload_path, verbose_name='Фото')),
                ('tag', models.ManyToManyField(blank=True, related_name='tags', to='places.PlaceTag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Место - куда пойти?',
                'verbose_name_plural': 'Места - куда пойти?',
                'ordering': ['-pk'],
            },
        ),
    ]
