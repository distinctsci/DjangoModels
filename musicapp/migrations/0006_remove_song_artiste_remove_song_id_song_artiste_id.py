# Generated by Django 4.1.2 on 2022-10-29 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musicapp", "0005_alter_lyric_id_alter_song_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="song", name="artiste",),
        migrations.RemoveField(model_name="song", name="id",),
        migrations.AddField(
            model_name="song",
            name="artiste_id",
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
