# Generated by Django 4.1.7 on 2023-11-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ddpui", "0028_orgwarehouse_superset_creds"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrefectFlowRun",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deployment_id", models.CharField(max_length=36)),
                ("flow_run_id", models.CharField(max_length=36)),
                ("name", models.CharField(max_length=255)),
                ("start_time", models.DateTimeField()),
                ("expected_start_time", models.DateTimeField()),
                ("total_run_time", models.FloatField()),
                ("status", models.CharField(max_length=20)),
                ("state_name", models.CharField(max_length=20)),
            ],
        ),
    ]