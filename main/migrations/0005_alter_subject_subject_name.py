# Generated by Django 4.2.9 on 2024-01-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_rename_subname_subject_subject_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject",
            name="subject_name",
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
