# Generated by Django 2.2.5 on 2019-10-03 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20191003_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='adddate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Add Time'),
        ),
    ]