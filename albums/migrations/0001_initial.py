# Generated by Django 2.2.5 on 2019-09-09 08:09

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
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('featuredesc', models.TextField(blank=True)),
                ('keyword', models.TextField(blank=True)),
                ('channel', models.CharField(default='1', max_length=255)),
                ('vdoname', models.CharField(blank=True, max_length=40)),
                ('flvdoname', models.CharField(blank=True, max_length=40)),
                ('formats', models.CharField(blank=True, max_length=500)),
                ('lformats', models.CharField(blank=True, max_length=500)),
                ('duration', models.FloatField(null=True)),
                ('space', models.BigIntegerField(default=0)),
                ('type', models.CharField(blank=True, max_length=7)),
                ('addtime', models.CharField(blank=True, max_length=20)),
                ('adddate', models.DateField(default='0000-00-00')),
                ('recorddate', models.DateField(default='0000-00-00')),
                ('location', models.TextField(blank=True)),
                ('country', models.CharField(blank=True, max_length=120)),
                ('vkey', models.CharField(blank=True, max_length=20)),
                ('viewnumber', models.BigIntegerField(default=0)),
                ('viewtime', models.DateTimeField(default='0000-00-00 00:00:00')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
