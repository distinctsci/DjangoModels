# Generated by Django 4.1.2 on 2022-10-29 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musicapp", "0008_alter_lyric_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lyric", name="content", field=models.CharField(max_length=18),
        ),
    ]