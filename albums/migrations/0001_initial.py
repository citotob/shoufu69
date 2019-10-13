# Generated by Django 2.2.5 on 2019-10-04 03:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Name')),
                ('tags', models.TextField(blank=True, verbose_name='Tags')),
                ('total_photos', models.BigIntegerField(default=0, verbose_name='Total photos')),
                ('total_views', models.BigIntegerField(default=0, verbose_name='Total Views')),
                ('type', models.CharField(choices=[('1', 'Public'), ('0', 'Private')], default='1', max_length=1, verbose_name='Type')),
                ('addtime', models.BigIntegerField(default=0, verbose_name='Addtime')),
                ('status', models.CharField(choices=[('0', 'Suspended'), ('1', 'Active')], default='1', max_length=1, verbose_name='Status')),
                ('adddate', models.DateTimeField(auto_now_add=True, verbose_name='Add Date')),
                ('rate', models.FloatField(default=0, verbose_name='Rate')),
                ('ratedby', models.BigIntegerField(default=0, verbose_name='Ratedby')),
                ('total_comments', models.BigIntegerField(default=0, verbose_name='Total Comments')),
                ('total_favorites', models.BigIntegerField(default=0, verbose_name='Total Favorites')),
                ('likes', models.BigIntegerField(default=0, verbose_name='Likes')),
                ('dislikes', models.BigIntegerField(default=0, verbose_name='Dislikes')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='no-img.jpg', upload_to='photo/%Y/%m/%d')),
                ('caption', models.CharField(default='', max_length=100, verbose_name='Caption')),
                ('total_views', models.BigIntegerField(default=0, verbose_name='Total Views')),
                ('total_comments', models.BigIntegerField(default=0, verbose_name='Total Comments')),
                ('status', models.CharField(choices=[('0', 'Suspended'), ('1', 'Active')], default='1', max_length=1, verbose_name='Status')),
                ('rate', models.FloatField(default=0, verbose_name='Rate')),
                ('ratedby', models.BigIntegerField(default=0, verbose_name='Ratedby')),
                ('total_favorites', models.BigIntegerField(default=0, verbose_name='Total Favorites')),
                ('type', models.CharField(choices=[('1', 'Public'), ('0', 'Private')], default='1', max_length=1, verbose_name='Type')),
                ('likes', models.BigIntegerField(default=0, verbose_name='Likes')),
                ('dislikes', models.BigIntegerField(default=0, verbose_name='Dislikes')),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Album')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
        migrations.CreateModel(
            name='PhotoRatingIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.IntegerField(default=0, verbose_name='IP')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Photo')),
            ],
            options={
                'verbose_name': 'PhotoRatingIp',
                'verbose_name_plural': 'PhotoRatingIp',
            },
        ),
        migrations.CreateModel(
            name='PhotoRatingId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Photo')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PhotoRatingId',
                'verbose_name_plural': 'PhotoRatingId',
            },
        ),
        migrations.CreateModel(
            name='PhotoFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(default='', max_length=15, verbose_name='Reason')),
                ('message', models.TextField(blank=True, verbose_name='Message')),
                ('add_date', models.DateField(default=datetime.date.today, verbose_name='Add Date')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Photo')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PhotoFlag',
                'verbose_name_plural': 'PhotoFlags',
            },
        ),
        migrations.CreateModel(
            name='PhotoFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Photo')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PhotoFavorite',
                'verbose_name_plural': 'PhotoFavorite',
            },
        ),
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('addtime', models.BigIntegerField(default=0, verbose_name='Addtime')),
                ('status', models.CharField(choices=[('0', 'Suspended'), ('1', 'Active')], default='1', max_length=1, verbose_name='Status')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Photo')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PhotoComment',
                'verbose_name_plural': 'PhotoComments',
            },
        ),
        migrations.CreateModel(
            name='AlbumCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150, verbose_name='Name')),
                ('slug', models.CharField(default='', max_length=120, verbose_name='Slug')),
                ('thumb', models.ImageField(default='no-img.jpg', upload_to='')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AlbumCategory',
                'verbose_name_plural': 'AlbumCategories',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.AlbumCategory'),
        ),
        migrations.AddField(
            model_name='album',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
