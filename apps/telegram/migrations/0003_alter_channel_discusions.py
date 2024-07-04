# Generated by Django 5.0.3 on 2024-07-03 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("telegram", "0002_channel_description_en_channel_description_ru_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="channel",
            name="discusions",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="discusion_channel",
                to="telegram.channeldiscusion",
            ),
        ),
    ]
