# Generated by Django 5.0.3 on 2024-07-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="is_premium",
            field=models.BooleanField(default=False),
        ),
    ]
