# Generated by Django 4.2.9 on 2024-03-07 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_alter_subject_subject_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="ref",
            field=models.SlugField(default="Mario"),
            preserve_default=False,
        ),
    ]
