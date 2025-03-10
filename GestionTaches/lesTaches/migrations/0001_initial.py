# Generated by Django 5.1.6 on 2025-02-26 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("name", models.CharField(max_length=250)),
                ("description", models.TextField()),
                ("created_date", models.DateField(auto_now_add=True)),
                ("closed", models.BooleanField(default=False)),
                ("due_date", models.DateField(null=True)),
                (
                    "schedule_date",
                    models.DateField(
                        default=datetime.datetime(2025, 3, 5, 22, 57, 39, 75505)
                    ),
                ),
            ],
        ),
    ]
