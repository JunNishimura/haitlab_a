# Generated by Django 3.0.6 on 2020-12-22 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostIdea',
            fields=[
                ('idea_id', models.AutoField(primary_key=True, serialize=False, verbose_name='アイデアID')),
                ('title', models.CharField(default='Idea Title', max_length=100, verbose_name='タイトル')),
                ('overview', models.TextField(blank=True, max_length=500, null=True, verbose_name='概要')),
                ('value', models.TextField(blank=True, max_length=500, null=True, verbose_name='価値')),
                ('background', models.TextField(blank=True, max_length=500, null=True, verbose_name='背景')),
                ('passion', models.TextField(blank=True, max_length=500, null=True, verbose_name='思い')),
                ('idea_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='投稿画像')),
                ('idea_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日')),
                ('state', models.CharField(max_length=100, verbose_name='状態')),
                ('target', models.CharField(blank=True, max_length=100, null=True, verbose_name='ターゲット')),
                ('offer', models.CharField(blank=True, max_length=100, null=True, verbose_name='人材募集')),
                ('deadline', models.CharField(blank=True, max_length=30, null=True, verbose_name='期日')),
                ('feedback_point', models.TextField(blank=True, max_length=100, null=True, verbose_name='フィードバック観点')),
                ('event_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Event', verbose_name='イベント')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='アイデア投稿ユーザ')),
            ],
            options={
                'db_table': 'Post_Idea',
            },
        ),
        migrations.CreateModel(
            name='ReputationMap',
            fields=[
                ('reputation_id', models.AutoField(primary_key=True, serialize=False, verbose_name='reputationのID')),
                ('interesting', models.IntegerField(blank=True, default=0, null=True, verbose_name='面白さ')),
                ('novelty', models.IntegerField(blank=True, default=0, null=True, verbose_name='新規性')),
                ('possibility', models.IntegerField(blank=True, default=0, null=True, verbose_name='実現可能性')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idea.PostIdea', verbose_name='反応先のアイデア')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='反応したユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False, verbose_name='フィードバックID')),
                ('feedback_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='コメント投稿日')),
                ('feedback', models.TextField(max_length=255, verbose_name='フィードバック')),
                ('idea_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idea.PostIdea', verbose_name='アイデアID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='フィードバックユーザ')),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
    ]
