# Generated by Django 5.1.7 on 2025-03-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MainApp", "0003_remove_profile_photo_customuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="photo",
            field=models.ImageField(default="default.jpg", upload_to="profile_pics/"),
        ),
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
