# Generated by Django 4.2.5 on 2023-10-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Football",
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
                ("name", models.CharField(help_text="FOOTBALL PLAYER", max_length=100)),
                ("jerseyno", models.IntegerField()),
                ("country", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("Yrs_Of_Exp", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
    ]
