# Generated by Django 2.2.12 on 2020-05-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_auto_20200525_1333"),
    ]

    operations = [
        migrations.CreateModel(
            name="GVfdfg",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tryr", models.BigIntegerField()),
            ],
        ),
    ]