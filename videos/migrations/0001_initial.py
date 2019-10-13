# Generated by Django 2.2.5 on 2019-10-04 03:28

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
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.IntegerField(default=0, verbose_name='Video ID')),
                ('title', models.CharField(max_length=191, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('featuredesc', models.TextField(blank=True, verbose_name='featuredesc')),
                ('keyword', models.TextField(blank=True, verbose_name='keyword')),
                ('channel', models.CharField(default='1', max_length=191, verbose_name='channel')),
                ('vdoname', models.CharField(blank=True, max_length=40, verbose_name='vdoname')),
                ('flvdoname', models.CharField(blank=True, max_length=40, verbose_name='flvdoname')),
                ('formats', models.CharField(blank=True, max_length=191, verbose_name='formats')),
                ('lformats', models.CharField(blank=True, max_length=191, verbose_name='lformats')),
                ('duration', models.FloatField(null=True, verbose_name='duration')),
                ('space', models.BigIntegerField(default=0, verbose_name='space')),
                ('type', models.CharField(choices=[('1', 'Public'), ('0', 'Private')], default='1', max_length=1, verbose_name='type')),
                ('addtime', models.CharField(blank=True, max_length=20, verbose_name='addtime')),
                ('adddate', models.DateTimeField(auto_now_add=True, verbose_name='Add Time')),
                ('recorddate', models.DateField(default=datetime.date.today, verbose_name='recorddate')),
                ('location', models.TextField(blank=True, verbose_name='location')),
                ('country', models.CharField(blank=True, max_length=120, verbose_name='country')),
                ('vkey', models.CharField(blank=True, max_length=20, verbose_name='vkey')),
                ('viewnumber', models.BigIntegerField(default=0, verbose_name='viewnumber')),
                ('viewtime', models.DateTimeField(auto_now_add=True, verbose_name='viewtime')),
                ('com_num', models.IntegerField(default=0, verbose_name='com_num')),
                ('fav_num', models.IntegerField(default=0, verbose_name='fav_num')),
                ('download_num', models.BigIntegerField(default=0, verbose_name='download_num')),
                ('featured', models.CharField(blank=True, max_length=3, verbose_name='featured')),
                ('ratedby', models.BigIntegerField(default=0, verbose_name='ratedby')),
                ('rate', models.FloatField(default=0, verbose_name='rate')),
                ('filehome', models.CharField(blank=True, max_length=120, verbose_name='filehome')),
                ('be_comment', models.CharField(blank=True, max_length=3, verbose_name='be_comment')),
                ('be_rated', models.CharField(blank=True, max_length=3, verbose_name='be_rated')),
                ('embed', models.CharField(default='enabled', max_length=8, verbose_name='embed')),
                ('embed_code', models.TextField(blank=True, verbose_name='Embed Code')),
                ('thumbs', models.SmallIntegerField(default=20, verbose_name='thumbs')),
                ('voter_id', models.CharField(blank=True, max_length=191, verbose_name='voter_id')),
                ('server', models.CharField(blank=True, max_length=191, verbose_name='server')),
                ('active', models.CharField(blank=True, max_length=1, verbose_name='active')),
                ('hd_filename', models.CharField(blank=True, max_length=20, verbose_name='hd_filename')),
                ('ipod_filename', models.CharField(blank=True, max_length=20, verbose_name='ipod_filename')),
                ('aspect_hd', models.CharField(default='0', max_length=10, verbose_name='aspect_hd')),
                ('width_hd', models.IntegerField(default=0, verbose_name='width_hd')),
                ('height_hd', models.IntegerField(default=0, verbose_name='height_hd')),
                ('aspect_sd', models.CharField(default='0', max_length=10, verbose_name='aspect_sd')),
                ('width_sd', models.IntegerField(default=0, verbose_name='width_sd')),
                ('height_sd', models.IntegerField(default=0, verbose_name='height_sd')),
                ('iphone', models.IntegerField(default=0, verbose_name='iphone')),
                ('hd', models.IntegerField(default=0, verbose_name='hd')),
                ('likes', models.BigIntegerField(default=0, verbose_name='likes')),
                ('dislikes', models.BigIntegerField(default=0, verbose_name='dislikes')),
                ('thumb', models.ImageField(default='no-img.jpg', upload_to='thumbnails/%Y/%m/%d', verbose_name='Thumbnails')),
                ('thumb_url', models.CharField(default='/', max_length=200, verbose_name='Thumb URL')),
                ('videofile', models.FileField(null=True, upload_to='videos/%Y/%m/%d', verbose_name='')),
                ('tags', models.TextField(blank=True, verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='VideoVoteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Video')),
            ],
            options={
                'verbose_name': 'VideoVoteUser',
                'verbose_name_plural': 'VideoVoteUsers',
            },
        ),
        migrations.CreateModel(
            name='VideoVoteIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.IntegerField(default=0, verbose_name='IP')),
                ('vid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Video')),
            ],
            options={
                'verbose_name': 'VideoVoteIp',
                'verbose_name_plural': 'VideoVoteIps',
            },
        ),
        migrations.CreateModel(
            name='VideoThumbnails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb', models.ImageField(default='no-img.jpg', upload_to='thumbnails/%Y/%m/%d', verbose_name='Thumbnails')),
                ('vid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Video')),
            ],
        ),
        migrations.CreateModel(
            name='VideoSubscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe_date', models.DateField(default=datetime.date.today, verbose_name='Subscribe Date')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'VideoSubscribe',
                'verbose_name_plural': 'VideoSubscribes',
            },
        ),
        migrations.CreateModel(
            name='VideoFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(default='', max_length=15, verbose_name='Reason')),
                ('message', models.TextField(blank=True, verbose_name='Message')),
                ('add_date', models.DateField(default=datetime.date.today, verbose_name='Add Date')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Video')),
            ],
            options={
                'verbose_name': 'VideoFlag',
                'verbose_name_plural': 'VideoFlags',
            },
        ),
        migrations.CreateModel(
            name='VideoComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name='comment')),
                ('addtime', models.BigIntegerField(default=0, verbose_name='addtime')),
                ('status', models.CharField(choices=[('0', '0'), ('1', '1')], default='1', max_length=1, verbose_name='status')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Video')),
            ],
            options={
                'verbose_name': 'VideoComment',
                'verbose_name_plural': 'VideoComments',
            },
        ),
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150, verbose_name='Name')),
                ('slug', models.CharField(default='', max_length=120, verbose_name='Slug')),
                ('thumb', models.ImageField(default='no-img.jpg', upload_to='')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'VideoCategory',
                'verbose_name_plural': 'VideoCategories',
            },
        ),
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.VideoCategory'),
        ),
        migrations.AddField(
            model_name='video',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
