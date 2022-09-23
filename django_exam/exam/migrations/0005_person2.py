# Generated by Django 4.1.1 on 2022-09-23 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam", "0004_album"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person2",
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
                ("name", models.CharField(max_length=60)),
                (
                    "shirt_size",
                    models.CharField(
                        choices=[("S", "Small"), ("M", "Medium"), ("L", "Large")],
                        max_length=1,
                    ),
                ),
            ],
            options={"db_table": "person2",},
        ),
    ]
