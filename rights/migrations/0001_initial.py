# Generated by Django 3.2.4 on 2021-07-01 12:03

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RightTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Тег (права детей)',
                'verbose_name_plural': 'Теги (права детей)',
                'ordering': ['name', 'slug'],
            },
        ),
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Право ребенка')),
                ('description', models.CharField(max_length=500, verbose_name='Описание права ребенка')),
                ('text', models.TextField(verbose_name='Основной текст права ребенка')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18, verbose_name='Цвет обложки на странице')),
                ('imageUrl', models.ImageField(blank=True, help_text='Добавить фото', upload_to='rights/', verbose_name='Фото')),
                ('tags', models.ManyToManyField(related_name='righttags', to='rights.RightTag')),
            ],
            options={
                'verbose_name': 'Право ребенка',
                'verbose_name_plural': 'Права детей',
                'ordering': ['title', 'id'],
            },
        ),
    ]
