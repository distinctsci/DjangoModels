# Generated by Django 4.1.2 on 2022-10-29 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musicapp", "0007_rename_artiste_id_song_id_song_artiste_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lyric", name="content", field=models.TextField(default=""),
        ),
    ]
