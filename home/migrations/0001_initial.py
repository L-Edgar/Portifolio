# Generated by Django 5.0.1 on 2024-07-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("image", models.ImageField(upload_to="pics")),
                ("status", models.BooleanField(default=True)),
                ("link", models.CharField(max_length=100)),
                ("type", models.CharField(max_length=10)),
            ],
        ),
    ]
