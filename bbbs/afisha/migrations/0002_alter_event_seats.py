# Generated by Django 3.2.5 on 2021-07-16 21:04


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='seats',
            field=models.PositiveIntegerField(verbose_name='Количество мест'),
        ),
    ]
