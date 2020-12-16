# Generated by Django 3.0.6 on 2020-12-16 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ユーザーID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='ユーザー名')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('prof_img', models.ImageField(blank=True, default='user/default.png', null=True, upload_to='user/', verbose_name='プロフィール画像')),
                ('intro', models.TextField(blank=True, max_length=300, null=True, verbose_name='自己紹介')),
                ('univ_name', models.CharField(max_length=30, verbose_name='大学名')),
                ('major', models.CharField(blank=True, max_length=50, null=True, verbose_name='学部・学科・専攻')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserFollowing',
            fields=[
                ('relation_id', models.AutoField(primary_key=True, serialize=False, verbose_name='関係ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('following_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventStock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ストックID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event', verbose_name='ユーザーが保存したイベント')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='保存したユーザー')),
            ],
        ),
    ]
