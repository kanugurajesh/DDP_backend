# Generated by Django 4.1.7 on 2024-01-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ddpui", "0037_userattributes_is_consultant"),
    ]

    operations = [
        migrations.AddField(
            model_name="org",
            name="is_demo",
            field=models.BooleanField(default=False),
        ),
    ]
