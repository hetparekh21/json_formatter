# Generated by Django 4.1.3 on 2022-12-07 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("json_main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="saved_jsons",
            name="user_id",
            field=models.ForeignKey(
                db_column="user_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="json_main.usermodel",
            ),
        ),
    ]