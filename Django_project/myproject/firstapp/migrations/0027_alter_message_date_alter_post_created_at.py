# Generated by Django 4.2.3 on 2023-10-05 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0026_alter_message_date_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 5, 15, 9, 16, 324336)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 5, 15, 9, 16, 324336)),
        ),
    ]