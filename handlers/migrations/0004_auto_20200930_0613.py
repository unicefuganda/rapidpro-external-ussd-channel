# Generated by Django 3.1.1 on 2020-09-30 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handlers', '0003_auto_20200930_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handler',
            name='request_format',
            field=models.TextField(),
        ),
    ]
