# Generated by Django 5.0.4 on 2024-06-25 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_contact_pricing'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(default=datetime.datetime(2024, 6, 25, 8, 36, 39, 345984, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
