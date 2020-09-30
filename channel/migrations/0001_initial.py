# Generated by Django 3.1.1 on 2020-09-30 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0002_auto_20200927_2056'),
        ('handlers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='USSDSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=30, unique=True)),
                ('status', models.CharField(default='In Progress', max_length=20)),
                ('badge', models.CharField(default='info', max_length=15)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('last_access_at', models.DateTimeField()),
                ('ended_at', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contact')),
                ('handler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handlers.handler')),
            ],
        ),
        migrations.CreateModel(
            name='USSDChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_on', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_active', models.BooleanField(default=True)),
                ('send_url', models.URLField(max_length=100)),
                ('rapidpro_receive_url', models.URLField(max_length=100)),
                ('timeout_after', models.IntegerField(default=10)),
                ('trigger_word', models.CharField(default='USSD', max_length=20)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ussdchannel_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ussdchannel_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
