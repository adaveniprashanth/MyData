# Generated by Django 4.2.3 on 2023-08-12 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0021_alter_message_date_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 12, 14, 17, 28, 823048, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 12, 19, 47, 28, 823048)),
        ),
    ]