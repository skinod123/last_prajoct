# Generated by Django 4.1.1 on 2022-09-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rockay", "0008_rename_regions_route_travel_type_alter_route_svyzb"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("mobile", models.CharField(max_length=100)),
                ("telegram", models.CharField(max_length=100)),
                ("whatsapp", models.CharField(max_length=100)),
                ("home", models.CharField(max_length=100)),
            ],
        ),
    ]