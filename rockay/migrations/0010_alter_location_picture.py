# Generated by Django 4.1.1 on 2022-09-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rockay", "0009_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="picture",
            field=models.ImageField(upload_to="last_praject/bye/static/"),
        ),
    ]