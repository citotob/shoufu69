# Generated by Django 2.2.5 on 2019-09-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_video_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_comments',
            name='addtime',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video_comments',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='video_comments',
            name='status',
            field=models.CharField(choices=[('0', '0'), ('1', '1')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='video',
            name='ratedby',
            field=models.BigIntegerField(default=0),
        ),
    ]
