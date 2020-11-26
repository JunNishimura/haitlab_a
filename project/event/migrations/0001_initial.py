# Generated by Django 3.0.6 on 2020-11-26 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False, verbose_name='イベントID')),
                ('event_name', models.CharField(max_length=50, verbose_name='イベント名')),
                ('event_detail', models.TextField(blank=True, max_length=1000, null=True, verbose_name='イベント概要')),
                ('event_schedule', models.DateField(verbose_name='開催日時')),
                ('event_url', models.URLField(verbose_name='イベントurl')),
            ],
        ),
    ]
