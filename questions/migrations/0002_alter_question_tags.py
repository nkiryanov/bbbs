# Generated by Django 3.2.5 on 2021-07-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='questions', to='questions.QuestionTag', verbose_name='Тэги'),
        ),
    ]
