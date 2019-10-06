# Generated by Django 2.2.5 on 2019-09-30 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20190929_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='tags',
            field=models.TextField(blank=True, verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='video',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/%Y/%m/%d', verbose_name=''),
        ),
    ]