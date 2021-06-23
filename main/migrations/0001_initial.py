# Generated by Django 3.2.4 on 2021-06-23 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='places.place', verbose_name='Место - куда пойти?')),
                ('questions', models.ManyToManyField(to='questions.Question', verbose_name='Вопросы')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'Главная страница',
            },
        ),
    ]
