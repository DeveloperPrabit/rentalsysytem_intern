# Generated by Django 5.1.7 on 2025-03-22 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("MainApp", "0004_profile_photo_delete_customuser"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
    ]
