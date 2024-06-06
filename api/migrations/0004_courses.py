# Generated by Django 4.1.2 on 2024-06-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_ability"),
    ]

    operations = [
        migrations.CreateModel(
            name="Courses",
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
                ("title", models.CharField(max_length=200)),
                ("url", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=400)),
                ("level", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
                ("review", models.CharField(max_length=100)),
                ("tags", models.CharField(max_length=500)),
                ("slugs", models.CharField(max_length=500)),
            ],
        ),
    ]