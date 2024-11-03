# Generated by Django 5.1.2 on 2024-10-30 14:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("models", "0002_alter_category_name_alter_feature_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="date_created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]