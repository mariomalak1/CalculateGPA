# Generated by Django 4.2.9 on 2024-03-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Authentication", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
