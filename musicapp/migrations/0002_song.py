# Generated by Django 4.1.2 on 2022-10-29 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musicapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Song",
            fields=[
                ("title", models.CharField(max_length=18)),
                ("date_released", models.DateField()),
                ("likes", models.IntegerField()),
                ("artiste_id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
