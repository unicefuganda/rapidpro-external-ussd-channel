# Generated by Django 3.1.1 on 2020-09-29 05:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_remove_ussdchannel_send_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='ussdchannel',
            name='send_url',
            field=models.URLField(default=datetime.datetime(2020, 9, 29, 5, 45, 23, 817284, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
