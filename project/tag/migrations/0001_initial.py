# Generated by Django 3.0.6 on 2021-01-11 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('idea', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False, verbose_name='タグID')),
                ('tag_name', models.CharField(max_length=20, verbose_name='タグ名')),
            ],
        ),
        migrations.CreateModel(
            name='UserTagMap',
            fields=[
                ('usertag_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ユーザータグのID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IdeaTagMap',
            fields=[
                ('ideatag_id', models.AutoField(primary_key=True, serialize=False, verbose_name='アイデアタグのID')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idea.PostIdea')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tag.Tag')),
            ],
        ),
    ]
