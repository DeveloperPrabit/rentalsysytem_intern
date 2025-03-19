# Generated by Django 5.1.7 on 2025-03-18 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                ("full_name", models.CharField(max_length=255)),
                ("full_address", models.TextField()),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("mobile", models.CharField(max_length=15)),
                ("password", models.CharField(max_length=255)),
                ("terms_of_use", models.BooleanField(default=False)),
                ("is_not_robert", models.BooleanField(default=False)),
            ],
        ),
    ]
