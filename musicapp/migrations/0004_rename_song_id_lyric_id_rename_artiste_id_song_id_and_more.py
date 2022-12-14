# Generated by Django 4.1.2 on 2022-10-29 03:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("musicapp", "0003_lyric"),
    ]

    operations = [
        migrations.RenameField(model_name="lyric", old_name="song_id", new_name="id",),
        migrations.RenameField(
            model_name="song", old_name="artiste_id", new_name="id",
        ),
        migrations.AddField(
            model_name="lyric",
            name="song",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="musicapp.song",
            ),
        ),
        migrations.AddField(
            model_name="song",
            name="artiste",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="musicapp.artiste",
            ),
        ),
        migrations.AlterField(
            model_name="artiste", name="age", field=models.IntegerField(default=18),
        ),
        migrations.AlterField(
            model_name="artiste",
            name="first_name",
            field=models.CharField(max_length=18, verbose_name="first name"),
        ),
        migrations.AlterField(
            model_name="artiste",
            name="last_name",
            field=models.CharField(max_length=18, verbose_name="last name"),
        ),
        migrations.AlterField(
            model_name="song",
            name="date_released",
            field=models.DateField(
                default=datetime.date.today, verbose_name="date released"
            ),
        ),
        migrations.AlterField(
            model_name="song", name="likes", field=models.IntegerField(default=0),
        ),
    ]
