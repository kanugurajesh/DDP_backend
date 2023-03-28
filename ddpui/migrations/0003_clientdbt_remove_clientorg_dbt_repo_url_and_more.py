# Generated by Django 4.1.7 on 2023-03-27 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ddpui", "0002_invitation"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClientDbt",
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
                ("gitrepo_url", models.CharField(max_length=100)),
                ("project_dir", models.CharField(max_length=200)),
                ("dbtversion", models.CharField(max_length=10)),
                ("targetname", models.CharField(max_length=10)),
                ("targettype", models.CharField(max_length=10)),
                ("targetschema", models.CharField(max_length=10)),
                ("host", models.CharField(max_length=100)),
                ("port", models.CharField(max_length=5)),
                ("username", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
                ("database", models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name="clientorg",
            name="dbt_repo_url",
        ),
        migrations.AddField(
            model_name="clientorg",
            name="dbt",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ddpui.clientdbt",
            ),
        ),
    ]
