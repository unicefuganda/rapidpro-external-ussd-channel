# Generated by Django 3.1.1 on 2021-03-01 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ussdchannel',
            name='trigger_word',
        ),
    ]
