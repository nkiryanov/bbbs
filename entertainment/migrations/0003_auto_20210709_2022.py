# Generated by Django 3.2.5 on 2021-07-09 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entertainment', '0002_rename_imagecaption_guide_image_caption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='imageUrl',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='guide',
            old_name='imageUrl',
            new_name='image_url',
        ),
    ]
