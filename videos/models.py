# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import datetime

# Create your models here.
@python_2_unicode_compatible
class Video(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=191)
    description = models.TextField(_('description'),blank=True)
    featuredesc = models.TextField(_('featuredesc'), blank=True)
    keyword = models.TextField(_('keyword'),blank=True)
    channel = models.CharField(_('channel'),max_length=191, default='1')
    vdoname = models.CharField(_('vdoname'),max_length=40, blank=True)
    flvdoname = models.CharField(_('flvdoname'),max_length=40, blank=True)
    formats = models.CharField(_('formats'),max_length=191, blank=True)
    lformats = models.CharField(_('lformats'),max_length=191, blank=True)
    duration = models.FloatField(_('duration'),null=True)
    space = models.BigIntegerField(_('space'),default=0)
    type = models.CharField(_('type'),max_length=7, blank=True)
    addtime = models.CharField(_('addtime'),max_length=20, blank=True)
    adddate = models.DateField(_('adddate'),default=datetime.date.today)
    recorddate = models.DateField(_('recorddate'),default=datetime.date.today)
    location = models.TextField(_('location'),blank=True)
    country = models.CharField(_('country'),max_length=120, blank=True)
    vkey = models.CharField(_('vkey'),max_length=20, blank=True)
    viewnumber = models.BigIntegerField(_('viewnumber'),default=0)
    viewtime = models.DateTimeField(_('viewtime'),auto_now_add=True)
    com_num = models.IntegerField(_('com_num'),default=0)
    fav_num = models.IntegerField(_('fav_num'),default=0)
    download_num = models.BigIntegerField(_('download_num'),default=0)
    featured = models.CharField(_('featured'),max_length=3, blank=True)
    ratedby = models.BigIntegerField(_('ratedby'),default=0)
    rate = models.FloatField(_('rate'),default=0)
    filehome = models.CharField(_('filehome'),max_length=120, blank=True)
    be_comment = models.CharField(_('be_comment'),max_length=3, blank=True)
    be_rated = models.CharField(_('be_rated'),max_length=3, blank=True)
    embed = models.CharField(_('embed'),max_length=8, default='enabled')
    embed_code = models.TextField(_('embed_code'),blank=True)
    thumb = models.SmallIntegerField(_('thumb'),default=1)
    thumbs = models.SmallIntegerField(_('thumbs'),default=20)
    voter_id = models.CharField(_('voter_id'),max_length=191, blank=True)
    server = models.CharField(_('server'),max_length=191, blank=True)
    active = models.CharField(_('active'),max_length=1, blank=True)
    hd_filename = models.CharField(_('hd_filename'),max_length=20, blank=True)
    ipod_filename = models.CharField(_('ipod_filename'),max_length=20, blank=True)
    aspect_hd = models.CharField(_('aspect_hd'),max_length=10, default='0')
    width_hd = models.IntegerField(_('width_hd'),default=0)
    height_hd = models.IntegerField(_('height_hd'),default=0)
    aspect_sd = models.CharField(_('aspect_sd'),max_length=10, default='0')
    width_sd = models.IntegerField(_('width_sd'),default=0)
    height_sd = models.IntegerField(_('height_sd'),default=0)
    iphone = models.IntegerField(_('iphone'),default=0)
    hd = models.IntegerField(_('hd'),default=0)
    likes = models.BigIntegerField(_('likes'),default=0)
    dislikes = models.BigIntegerField(_('dislikes'),default=0)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return ''

class VideoComment(models.Model):
    vid = models.ForeignKey(Video, on_delete=models.CASCADE)
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(_('comment'),blank=True)
    addtime = models.BigIntegerField(_('addtime'),default=0)
    STATUS_ = (
        ('0','0'),
        ('1','1')
    )
    status = models.CharField(_('status'),max_length=1, choices=STATUS_,default='1')

    class Meta:
        verbose_name = 'VideoComment'
        verbose_name_plural = 'VideoComments'
        #unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return ''
    