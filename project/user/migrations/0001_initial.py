# Generated by Django 3.1.2 on 2020-11-07 05:29

from django.db import migrations, models
import multiselectfield.db.fields
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='タグ名')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='メールアドレス')),
                ('username', models.CharField(max_length=20, verbose_name='ユーザー名')),
                ('prof_img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='プロフィール画像')),
                ('intro', models.TextField(blank=True, max_length=300, null=True, verbose_name='自己紹介')),
                ('univ_name', models.CharField(max_length=30, verbose_name='大学名')),
                ('major', models.CharField(blank=True, max_length=50, null=True, verbose_name='学部・学科・専攻')),
                ('skills', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('デザイン', 'デザイン'), ('エンジニア', 'エンジニア'), ('英語', '英語'), ('マーケティング', 'マーケティング')], max_length=30, null=True)),
                ('contact', models.EmailField(blank=True, max_length=255, null=True, verbose_name='連絡先')),
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
    ]