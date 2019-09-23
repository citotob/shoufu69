# Generated by Django 2.2.5 on 2019-09-23 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
    ]