# Generated by Django 3.2.5 on 2021-07-13 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0012_auto_20210713_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='tags',
            new_name='tag',
        ),
    ]
