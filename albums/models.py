# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class video(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    featuredesc = models.TextField(blank=True)
    keyword = models.TextField(blank=True)
    channel = models.CharField(max_length=255, default='1')
    vdoname = models.CharField(max_length=40, blank=True)
    flvdoname = models.CharField(max_length=40, blank=True)
    formats = models.CharField(max_length=500, blank=True)
    lformats = models.CharField(max_length=500, blank=True)
    duration = models.FloatField(null=True)
    space = models.BigIntegerField(default=0)
    type = models.CharField(max_length=7, blank=True)
    addtime = models.CharField(max_length=20, blank=True)
    adddate = models.DateField(default='0000-00-00')
    recorddate = models.DateField(default='0000-00-00')
    location = models.TextField(blank=True)
    country = models.CharField(max_length=120, blank=True)
    vkey = models.CharField(max_length=20, blank=True)
    viewnumber = models.BigIntegerField(default=0)
    viewtime = models.DateTimeField(default='0000-00-00 00:00:00')
    com_num = models.IntegerField(default=0)
    fav_num = models.IntegerField(default=0)
    download_num = models.BigIntegerField(default=0)
    featured = models.CharField(max_length=3, blank=True)
    ratedby = models.BigIntegerField(default=0)
    rate = models.FloatField(default=0)
    filehome = models.CharField(max_length=120, blank=True)
    be_comment = models.CharField(max_length=3, blank=True)
    be_rated = models.CharField(max_length=3, blank=True)
    embed = models.CharField(max_length=8, default='enabled')
    embed_code = models.TextField(blank=True)
    thumb = models.SmallIntegerField(default=1)
    thumbs = models.SmallIntegerField(default=20)
    voter_id = models.CharField(max_length=200, blank=True)
    server = models.CharField(max_length=255, blank=True)
    active = models.CharField(max_length=1, blank=True)
    hd_filename = models.CharField(max_length=20, blank=True)
    ipod_filename = models.CharField(max_length=20, blank=True)
    aspect_hd = models.CharField(max_length=10, default='0')
    width_hd = models.IntegerField(default=0)
    height_hd = models.IntegerField(default=0)
    aspect_sd = models.CharField(max_length=10, default='0')
    width_sd = models.IntegerField(default=0)
    height_sd = models.IntegerField(default=0)
    iphone = models.IntegerField(default=0)
    hd = models.IntegerField(default=0)
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)

class video_comments(models.Model):
    vid = models.ForeignKey(video, on_delete=models.CASCADE)
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    addtime = models.BigIntegerField(default=0)
    STATUS_ = (
        ('0','0'),
        ('1','1')
    )
    status = models.CharField(max_length=1, choices=STATUS_,default='1')
    