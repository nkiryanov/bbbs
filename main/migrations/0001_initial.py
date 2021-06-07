# Generated by Django 3.2.3 on 2021-06-05 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("places", "0001_initial"),
        ("questions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Main",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="places.place",
                    ),
                ),
                ("questions", models.ManyToManyField(to="questions.Question")),
            ],
        ),
    ]
